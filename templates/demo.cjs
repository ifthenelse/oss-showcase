const { chromium } = require("playwright");
const { mkdtemp, rm } = require("node:fs/promises");
const { tmpdir } = require("node:os");
const { join } = require("node:path");

async function record() {
  const url = new URL(process.argv[2]);
  if (url.protocol !== "http:" || url.hostname !== "127.0.0.1" || url.username || url.password) {
    throw new Error("Use the local fixture HTTP server on 127.0.0.1.");
  }
  const directory = await mkdtemp(join(tmpdir(), "showcase-video-"));
  let browser;
  try {
    browser = await chromium.launch();
    const size = { width: 1280, height: 720 };
    const context = await browser.newContext({
      viewport: size,
      recordVideo: { dir: directory, size },
      serviceWorkers: "block",
      acceptDownloads: false,
    });
    await context.route("**/*", (route) => (
      new URL(route.request().url()).origin === url.origin ? route.continue() : route.abort()
    ));
    await context.routeWebSocket("**/*", (socket) => socket.close());
    const page = await context.newPage();
    const response = await page.goto(url.href);
    if (!response?.ok()) throw new Error("Fixture page failed to load.");
    // Add the verified flow here and wait for its actual final UI state.
    throw new Error("Fill in and verify the project-specific recording steps first.");
    // await context.close();
    // await page.video().saveAs("demo.webm");
  } finally {
    if (browser) await browser.close();
    await rm(directory, { recursive: true, force: true });
  }
}

record().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
