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

function backMain(app) {
  openAppSetting(app);
  sleep(1000);
  id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
  sleep(1000);
  click("确定");
  sleep(1000);
  back();
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

  sleep(1000);
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
  var athene_cancle_result = waitForImage(athene_cancle, 15000);
  athene_cancle.recycle();

  if (athene_cancle_result) {
    click(athene_cancle_result.x, athene_cancle_result.y);
  }

  // 判断是否签到
  var athene_sign = images.read("./appStartUp/athene_sign.png");
  var athene_sign_result = waitForImage(athene_sign, 15000);
  athene_sign.recycle();

  if (athene_sign_result) {
    click(athene_sign_result.x, athene_sign_result.y);
    sleep(10000);
  }

  // 进入挖矿页
  var athene_main = images.read("./appStartUp/athene_main.png");
  var athene_main_result = waitForImage(athene_main, 15000);
  athene_main.recycle();

  if (athene_main_result) {
    click(athene_main_result.x, athene_main_result.y);

    // 判断是否开始
    var athene_startup = images.read("./appStartUp/athene_startup.png");
    var athene_startup_result = waitForImage(athene_startup, 15000);
    athene_startup.recycle();

    if (athene_startup_result) {
      click(athene_startup_result.x, athene_startup_result.y);
      sleep(1000);
    }

    // 判断是否领取
    var athene_rewards = images.read("./appStartUp/athene_rewards.png");
    var athene_rewards_result = waitForImage(athene_rewards, 15000);
    athene_rewards.recycle();

    if (athene_rewards_result) {
      click(athene_rewards_result.x, athene_rewards_result.y);
      sleep(1000);
    }

    var athene_main = images.read("./appStartUp/athene_main.png");
    if (!waitForImage(athene_main, 15000)) {
      sleep(1000);
      click(150, 2190);
    }
    athene_main.recycle();
  }

  sleep(1000);
  home();
}

function AZCoinerStart() {
  app.launch("com.azc.azcoiner");
  waitForPackage("com.azc.azcoiner");

  if (!requestScreenCapture()) {
    toast("请求截图权限失败");
    exit();
  }

  // 判断是否进入应用
  var azcoiner_index = images.read("./appStartUp/azcoiner_index.png");
  var azcoiner_index_result = waitForImage(azcoiner_index, 60000);
  azcoiner_index.recycle();

  if (azcoiner_index_result) {
    // 判断是否开始挖矿
    var azcoiner_startup = images.read("./appStartUp/azcoiner_startup.png");
    var azcoiner_startup_result = waitForImage(azcoiner_startup, 60000);
    azcoiner_startup.recycle();

    if (azcoiner_startup_result) {
      // 开始挖矿
      click(azcoiner_startup_result.x, azcoiner_startup_result.y);
    }
  }

  sleep(1000);
  home();
}

function NovaStart() {
  app.launch("one.novaverse.android");
  waitForPackage("one.novaverse.android");

  if (!requestScreenCapture()) {
    toast("请求截图权限失败");
    exit();
  }

  // 判断有无额外页
  var nova_index_flag = images.read("./appStartUp/nova_index_flag.png");
  var nova_index_flag_result = waitForImage(nova_index_flag, 60000);
  nova_index_flag.recycle();

  if (nova_index_flag_result) {
    back();
  }

  // 判断是否进入应用
  var nova_index = images.read("./appStartUp/nova_index.png");
  var nova_index_result = waitForImage(nova_index, 10000);
  nova_index.recycle();

  if (nova_index_result) {
    // 判断是否进入挖矿页
    var nova_click = images.read("./appStartUp/nova_click.png");
    var nova_click_result = waitForImage(nova_click, 10000);
    nova_click.recycle();

    if (nova_click_result) {
      click(nova_click_result.x, nova_click_result.y);
      sleep(1000);

      // 判断是否开始挖矿
      var nova_startup = images.read("./appStartUp/nova_startup.png");
      var nova_startup_result = waitForImage(nova_startup, 10000);
      nova_startup.recycle();

      if (nova_startup_result) {
        click(nova_startup_result.x, nova_startup_result.y);

        // 关闭会员提示
        let nova_cancle = images.read("./appStartUp/nova_cancle.png");
        let nova_cancle_result = waitForImage(nova_cancle, 10000);
        nova_cancle.recycle();

        if (nova_cancle_result) {
          click(nova_cancle_result.x, nova_cancle_result.y);
          sleep(1000);
        }
      }

      // 判断是否可以加速
      swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 3) * y, 500);

      var nova_rewards = images.read("./appStartUp/nova_rewards.png");
      var nova_rewards_result = waitForImage(nova_rewards, 10000);
      nova_rewards.recycle();

      if (nova_rewards_result) {
        click(nova_rewards_result.x, nova_rewards_result.y);
        sleep(1000);

        // 开始抽取加速
        var nova_rewards_start = images.read("./appStartUp/nova_rewards_start.png");
        var nova_rewards_start_result = waitForImage(nova_rewards_start, 10000);
        nova_rewards_start.recycle();

        if (nova_rewards_start_result) {
          click(nova_rewards_start_result.x, nova_rewards_start_result.y);
          sleep(1000);

          // 确认抽取加速
          var nova_rewards_confirm = images.read("./appStartUp/nova_rewards_confirm.png");
          var nova_rewards_confirm_result = waitForImage(nova_rewards_confirm, 10000);
          nova_rewards_confirm.recycle();

          if (nova_rewards_confirm_result) {
            click(nova_rewards_confirm_result.x, nova_rewards_confirm_result.y);
            sleep(1000);
          }
        }

        // 关闭会员提示
        let nova_cancle = images.read("./appStartUp/nova_cancle.png");
        let nova_cancle_result = waitForImage(nova_cancle, 10000);
        nova_cancle.recycle();

        if (nova_cancle_result) {
          click(nova_cancle_result.x, nova_cancle_result.y);
          sleep(1000);
        }
      }

      swipe((2 / 3) * x, (1 / 3) * y, (2 / 3) * x, (2 / 3) * y, 500);
    }

    // 进入签到页
    sleep(2000);
    click(975, 2230);
    sleep(2000);
    click(936, 242);

    // 判断是否可以签到
    var nova_sign_flag = images.read("./appStartUp/nova_sign_flag.png");
    var nova_sign_flag_result = waitForImage(nova_sign_flag, 10000);
    nova_sign_flag.recycle();

    if (!nova_sign_flag_result) {
      click(535, 2190);
      sleep(2000);
      click(535, 1460);

      // 关闭会员提示
      let nova_cancle = images.read("./appStartUp/nova_cancle.png");
      let nova_cancle_result = waitForImage(nova_cancle, 10000);
      nova_cancle.recycle();

      if (nova_cancle_result) {
        click(nova_cancle_result.x, nova_cancle_result.y);
        sleep(1000);
      }
    }

    // 退出签到页
    sleep(2000);
    click(79, 173);

    // 回到首页
    sleep(1000);
    click(106, 2230);
  }

  sleep(1000);
  home();
}

function CeliaStart() {
  app.launch("com.celia.finance");
  waitForPackage("com.celia.finance");

  if (!requestScreenCapture()) {
    toast("请求截图权限失败");
    exit();
  }

  sleep(10000);
  click(1030, 1288);

  // 判断是否开始挖矿
  var celia_startup = images.read("./appStartUp/celia_startup.png");
  var celia_startup_result = waitForImage(celia_startup, 10000);
  celia_startup.recycle();

  if (celia_startup_result) {
    click(celia_startup_result.x, celia_startup_result.y);
    sleep(2000);
    click(527, 1449);
  }

  sleep(1000);
  back();
  sleep(1000);
  home();
}

function sign_115() {
  app.launch("com.ylmf.androidclient");
  waitForPackage("com.ylmf.androidclient");

  if (!requestScreenCapture()) {
    toast("请求截图权限失败");
    exit();
  }

  // 判断是否进入应用
  var index_115 = images.read("./appStartUp/index_115.png");
  var index_115_result = waitForImage(index_115, 10000);
  index_115.recycle();

  if (index_115_result) {
    click(index_115_result.x, index_115_result.y);

    // 签到
    var sign_115 = images.read("./appStartUp/sign_115.png");
    var sign_115_result = waitForImage(sign_115, 10000);
    sign_115.recycle();

    if (!sign_115_result) {
      click(148, 158);

      var sign_115_flag = images.read("./appStartUp/sign_115_flag.png");
      var sign_115_flag_result = waitForImage(sign_115_flag, 10000);
      sign_115_flag.recycle();

      if (sign_115_flag_result) {
        click(sign_115_flag_result.x, sign_115_flag_result.y);
      }
    }
  }

  sleep(1000);
  backMain("com.ylmf.androidclient");
}

function main() {
  device.wakeUp();
  auto.waitFor();

  sleep(1000);
  phonepalStart();
  sleep(1000);
  traffmonetizerStart();
  sleep(1000);
  sign_115();

  sleep(1000);
  cPenStart();
  sleep(1000);
  atheneStart();
  sleep(1000);
  AZCoinerStart();
  sleep(1000);
  CeliaStart();
  sleep(1000);
  NovaStart();
  // sleep(1000);
  // NovaStart();
}

const x = 1080;
const y = 2340;

main();
