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

function run() {
  var kuaishou_yuyue = images.read("./kuaishou/kuaishou_pre_yuyue.png");
  var kuaishou_yuyue_point = waitForImage(kuaishou_yuyue, 5000);
  kuaishou_yuyue.recycle();

  if (kuaishou_yuyue_point) {
    var kuaishou_yuyue_flag = images.read("./kuaishou/kuaishou_pre_yuyue_flag.png");
    var kuaishou_yuyue_flag_point = waitForRegionImage(kuaishou_yuyue_flag, kuaishou_yuyue_point.x, kuaishou_yuyue_point.y, 970, 148, 3000);
    kuaishou_yuyue_flag.recycle();

    if (kuaishou_yuyue_flag_point) {
      click(kuaishou_yuyue_flag_point.x, kuaishou_yuyue_flag_point.y);

      sleep(10000);

      var kuaishou_yuyue_wards = images.read("./kuaishou/kuaishou_pre_yuyue_wards.png");
      var kuaishou_yuyue_wards_point = waitForImage(kuaishou_yuyue_wards, 5000);
      kuaishou_yuyue_wards.recycle();

      if (kuaishou_yuyue_wards_point) {
        click(kuaishou_yuyue_wards_point.x, kuaishou_yuyue_wards_point.y);
        sleep(5000);
        back();
      }
    }
  }
}

function main() {
  run();
}

if (!requestScreenCapture()) {
  toast("请求截图权限失败");
  exit();
}

const x = 1080;
const y = 2340;

main();
