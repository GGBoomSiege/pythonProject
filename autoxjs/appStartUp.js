// 定义一个函数来等待图片出现 (普通图片)
function waitForImage(image, timeout, threshold) {
  threshold = threshold || 0.9;
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image, {
      threshold: threshold,
    });
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

  var cpen_startup = images.read("./appStartUp/cpen_startup.png");
  var cpen_startup_result = waitForImage(cpen_startup, 10000);
  cpen_startup.recycle();

  if (cpen_startup_result) {
    click(cpen_startup_result.x + 152 / 2, cpen_startup_result.y + 152 / 2);
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

function atheneStart() {
  app.launch("network.athene.app");
  waitForPackage("network.athene.app");

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  // 判断是否进入应用
  var athene_index = images.read("./appStartUp/athene_index.png");
  var athene_index_result = waitForImage(athene_index, 60000, 0.8);
  athene_index.recycle();

  if (athene_index_result) {
    log(athene_index_result.x, athene_index_result.y);
  }

  // 判断是否有额外页面
  var athene_cancle = images.read("./appStartUp/athene_cancle.png");
  var athene_cancle_result = waitForImage(athene_cancle, 10000);
  athene_cancle.recycle();

  if (athene_cancle_result) {
    click(athene_cancle_result.x, athene_cancle_result.y);
  }

  // 判断是否签到
  var athene_sign = images.read("./appStartUp/athene_sign.png");
  var athene_sign_result = waitForImage(athene_sign, 10000);
  athene_sign.recycle();

  if (athene_sign_result) {
    click(athene_sign_result.x, athene_sign_result.y);
  }

  // 进入挖矿页
  var athene_main = images.read("./appStartUp/athene_main.png");
  var athene_main_result = waitForImage(athene_main, 10000);
  athene_main.recycle();

  if (athene_main_result) {
    click(athene_main_result.x, athene_main_result.y);

    // 判断是否开始
    var athene_startup = images.read("./appStartUp/athene_startup.png");
    var athene_startup_result = waitForImage(athene_startup, 10000);
    athene_startup.recycle();

    if (athene_startup_result) {
      click(athene_startup_result.x, athene_startup_result.y);
      sleep(1000);
    }

    // 判断是否领取
    var athene_rewards = images.read("./appStartUp/athene_rewards.png");
    var athene_rewards_result = waitForImage(athene_rewards, 10000);
    athene_rewards.recycle();

    if (athene_rewards_result) {
      click(athene_rewards_result.x, athene_rewards_result.y);
      sleep(1000);
    }

    click(150, 2190);
  }

  home();
}

function AZCoinerStart() {
  app.launch("com.azc.azcoiner");
  waitForPackage("com.azc.azcoiner");
}

function NovaStart() {
  app.launch("one.novaverse.android");
  waitForPackage("one.novaverse.android");

  if (!requestScreenCapture()) {
    toast("请求截图权限失败");
    exit();
  }

  var nova_main = images.read("./appStartUp/nova_main.png");
  var nova_main_result = waitForImage(nova_main, 60000);
  nova_main.recycle();

  if (nova_main_result) {
    var nova_click = images.read("./appStartUp/nova_click.png");
    var nova_click_result = waitForImage(nova_click, 10000);
    nova_click.recycle();

    if (nova_click_result) {
      click(nova_click_result.x, nova_click_result.y);
      sleep(1000);

      var nova_startup = images.read("./appStartUp/nova_startup.png");
      var nova_startup_result = waitForImage(nova_startup, 10000);
      nova_startup.recycle();

      if (nova_startup_result) {
        click(nova_startup_result.x, nova_startup_result.y);

        var nova_cancle = images.read("./appStartUp/nova_cancle.png");
        var nova_cancle_result = waitForImage(nova_cancle, 10000);
        nova_cancle.recycle();

        if (nova_cancle_result) {
          click(nova_cancle_result.x, nova_cancle_result.y);
          sleep(1000);
        }
      }
    }

    sleep(1000);
    click(106, 2230);
  }
  home();
}

function main() {
  device.wakeUp();
  auto.waitFor();

  sleep(1000);
  phonepalStart();
  sleep(1000);
  traffmonetizerStart();

  sleep(1000);
  cPenStart();
  sleep(1000);
  atheneStart();
  // sleep(1000);
  // AZCoinerStart();
  sleep(1000);
  NovaStart();
  // sleep(1000);
  // NovaStart();
}

const x = device.width;
const y = device.height;

main();
