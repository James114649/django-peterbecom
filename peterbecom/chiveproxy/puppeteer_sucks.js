const puppeteer = require('puppeteer');

if (process.argv.length < 3) {
  console.warn('Missing URL argument');
  process.exit(1);
}
const url = process.argv[2];

(async url => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
    defaultViewport: {
      width: 1920,
      height: 2080
    }
  });
  const page = await browser.newPage();
  page.setDefaultTimeout(15000);
  let response;
  try {
    response = await page.goto(url, {
      timeout: 25000,
      waitUntil: 'networkidle2'
    });
  } catch (er) {
    console.warn(`Failed to goto ${url}`, er);
    await browser.close();
    process.exit(2);
  }
  let exit = 0;
  if (response && response.ok()) {
    await page.waitFor(2000);
    // await page.screenshot({ path: '/tmp/screenshot.png' });
    let html = await page.content();
    console.log(html);
  } else if (!response) {
    console.warn(`Response was null for ${url}`);
    exit = 3;
  } else {
    console.warn(`Response was ${response.status()} for ${url}`);
    exit = 4;
  }
  await browser.close();
  process.exit(exit);
})(url);
