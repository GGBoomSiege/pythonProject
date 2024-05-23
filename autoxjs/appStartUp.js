// 定义一个函数来等待图片出现 (普通图片)
function waitForImage(image, timeout) {
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image);
    screenshot.recycle();
    if (found) {
      return found;
    }
    if (Date.now() - startTime > timeout) {
      log("等待超时");
      return null;
    }
    sleep(1000); // 每秒检查一次
  }
}

function cPenStart() {
  app.launch("io.cpen.mobile");
  waitForPackage("io.cpen.mobile");

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  var startup = images.read("./cpen/startup.png");
  var result = waitForImage(startup, 10000);
  startup.recycle();

  if (result) {
    click(result.x + 152 / 2, result.y + 152 / 2);
    toastLog("运行完成!");
  } else {
    toastLog("未找到指定图片");
  }

  home();
}

function phonepalStart() {
  app.launch("net.onething.phonepal");
  sleep(10000);
  home();
}

function traffmonetizerStart() {
  app.launch("com.traffmonetizer.client");
  sleep(10000);
  home();
}

function main() {
  device.wakeUp();
  sleep(1000);
  phonepalStart();
  sleep(1000);
  cPenStart();
  sleep(1000);
  traffmonetizerStart();
}

main();
