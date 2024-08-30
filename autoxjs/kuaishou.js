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

// 定义一个函数来等待图片出现 (灰度图片)
function waitForGrayscaleImage(image, timeout, threshold) {
  threshold = threshold || 0.9;
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(images.grayscale(screenshot), images.grayscale(image), {
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

// 定义一个函数来等待图片出现 (区域找图)
function waitForRegionImage(image, x, y, width, height, timeout, threshold) {
  threshold = threshold || 0.9;
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image, {
      region: [x, y, width, height],
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

function backMain(package) {
  openAppSetting(package);
  sleep(2000);
  id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
  sleep(2000);
  click("确定");
  sleep(2000);
  back();
}

function runMain(package) {
  app.launch(package);
  waitForPackage(package);
  sleep(3000);
  back();
}

//   看广告赚金币

function kuaishou_ad() {
  log("广告开始");
  var ad_count = 0;
  while (ad_count++ < 30) {
    var kuaishou_ad_pre_success = images.read("./kuaishou/kuaishou_ad_pre_success.png");
    var kuaishou_ad_pre_success_point = waitForGrayscaleImage(kuaishou_ad_pre_success, 5000);
    kuaishou_ad_pre_success.recycle();

    if (kuaishou_ad_pre_success_point) {
      click(kuaishou_ad_pre_success_point.x, kuaishou_ad_pre_success_point.y);
    }

    var kuaishou_ad_success = images.read("./kuaishou/kuaishou_ad_success.png");
    var kuaishou_ad_success_point = waitForGrayscaleImage(kuaishou_ad_success, 60000);
    kuaishou_ad_success.recycle();

    if (kuaishou_ad_success_point) {
      click(kuaishou_ad_success_point.x, kuaishou_ad_success_point.y);
      sleep(1000);

      var kuaishou_ad_continue = images.read("./kuaishou/kuaishou_ad_continue.png");
      var kuaishou_ad_continue_point = waitForGrayscaleImage(kuaishou_ad_continue, 5000);
      kuaishou_ad_continue.recycle();

      if (kuaishou_ad_continue_point) {
        click(kuaishou_ad_continue_point.x, kuaishou_ad_continue_point.y);
      }
    }

    var kuaishou_ad_flag = images.read("./kuaishou/kuaishou_ad_flag.png");
    var kuaishou_ad_flag_point = waitForImage(kuaishou_ad_flag, 5000);
    kuaishou_ad_flag.recycle();

    if (kuaishou_ad_flag_point) {
      log("广告结束");
      break;
    }
  }
}

function run() {
  var run_count = 0;
  while (run_count++ < 10) {
    var kuaishou_ad_flag = images.read("./kuaishou/kuaishou_ad_flag.png");
    var kuaishou_ad_flag_point = waitForImage(kuaishou_ad_flag, 3000);
    kuaishou_ad_flag.recycle();

    if (kuaishou_ad_flag_point) {
      run_count = 0;
      while (run_count++ < 20) {
        var kuaishou_ad_flag = images.read("./kuaishou/kuaishou_ad_flag.png");
        var kuaishou_ad_flag_point = waitForImage(kuaishou_ad_flag, 3000);
        kuaishou_ad_flag.recycle();

        if (kuaishou_ad_flag_point) {
          log("开始领取广告福利");
          var kuaishou_ad_startup = images.read("./kuaishou/kuaishou_ad_startup.png");
          var kuaishou_ad_startup_point = waitForRegionImage(kuaishou_ad_startup, kuaishou_ad_flag_point.x, kuaishou_ad_flag_point.y, 972, 154, 3000);
          kuaishou_ad_startup.recycle();

          if (kuaishou_ad_startup_point) {
            sleep(3000);
            click(kuaishou_ad_startup_point.x, kuaishou_ad_startup_point.y);
            sleep(3000);
            kuaishou_ad(); // 点击广告
          } else {
            swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 2) * y, 500);
            sleep(2000);
          }
        } else {
          log("结束领取广告福利");
          break;
        }

        sleep(2000);
        if (run_count === 20) {
          log("脚本运行失败");
        }
      }
      break;
    }

    swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 2) * y, 500);
    sleep(2000);
  }
}

function main() {
  runMain("com.kuaishou.nebula");
  sleep(5000);
  backMain("com.kuaishou.nebula");

  sleep(5000);
  runMain("com.kuaishou.nebula");
  sleep(5000);
  // 点击去赚钱
  click(756, 2230);
  sleep(10000);
  backMain("com.kuaishou.nebula");

  sleep(5000);
  runMain("com.kuaishou.nebula");
  sleep(5000);
  // 点击去赚钱
  click(756, 2230);
  sleep(10000);
  backMain("com.kuaishou.nebula");

  sleep(5000);
  runMain("com.kuaishou.nebula");
  sleep(5000);
  // 点击去赚钱
  click(756, 2230);
  sleep(20000);
  run();
  sleep(5000);
  backMain("com.kuaishou.nebula");
}

if (!requestScreenCapture()) {
  toast("请求截图权限失败");
  exit();
}

const x = 1080;
const y = 2340;

device.wakeUp();
auto.waitFor();
main();
