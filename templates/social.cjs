const { readFile } = require("node:fs/promises");
const { resolve, join } = require("node:path");
const { chromium } = require("playwright");

async function render() {
  const [factsPath, cardPath, outputPath, root = "."] = process.argv.slice(2);
  const facts = JSON.parse(await readFile(factsPath, "utf8"));
  if (!facts.name?.trim() || !facts.summary?.trim()) {
    throw new Error("Provide a verified project name and summary.");
  }
  const card = await readFile(cardPath, "utf8");
  let logo;
  const source = facts.assets?.logo?.path;
  if (source) {
    const match = /^assets\/(?:[A-Za-z0-9_-]+\/)*[A-Za-z0-9_.-]+\.(svg|png|webp)$/.exec(source);
    if (!match) throw new Error("Use a reviewed local logo under docs/assets.");
    const mime = match[1] === "svg" ? "image/svg+xml" : `image/${match[1]}`;
    const bytes = await readFile(join(resolve(root), "docs", source));
    logo = `data:${mime};base64,${bytes.toString("base64")}`;
  }
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 640 } });
    await page.route("**/*", (route) => route.abort());
    await page.setContent(card);
    await page.evaluate(({ name, summary, logo }) => {
      document.querySelector("#product").textContent = name;
      document.querySelector("#tagline").textContent = summary;
      if (logo) {
        const image = document.createElement("img");
        image.alt = "";
        image.src = logo;
        document.querySelector("main").prepend(image);
      }
    }, { name: facts.name, summary: facts.social_tagline || facts.summary, logo });
    if (logo) await page.locator("main img").evaluate((image) => image.decode());
    await page.evaluate(() => document.fonts.ready);
    if (!await page.locator("main").evaluate((element) =>
      element.scrollHeight <= element.clientHeight && element.scrollWidth <= element.clientWidth)) {
      throw new Error("Social card content overflows. Shorten the tagline or adjust the template.");
    }
    await page.screenshot({ path: outputPath, type: "png" });
  } finally {
    await browser.close();
  }
}

render().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
