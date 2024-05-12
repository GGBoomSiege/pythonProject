function cPenStart() {
  app.launch("io.cpen.mobile");
  waitForPackage("io.cpen.mobile");
  sleep(10000);
  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }
  var img = captureScreen();
  var startup = images.read("./cpen/startup.png");
  var result = findImage(img, startup);

  if (result === null) {
    toastLog("未找到指定图片");
  } else {
    click(result.x + 152 / 2, result.y + 152 / 2);
    toastLog("运行完成!");
  }

  startup.recycle();
  img.recycle();
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
  sleep(2000);
  phonepalStart();
  sleep(2000);
  cPenStart();
  sleep(2000);
  traffmonetizerStart();
}

main();
