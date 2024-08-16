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

//   看广告赚金币

function kuaishou_ad() {
  log("广告开始");
  while (true) {
    var kuaishou_ad_success = images.read("./kuaishou/kuaishou_ad_success.png");
    var kuaishou_ad_success_point = waitForGrayscaleImage(kuaishou_ad_success, 60000);
    kuaishou_ad_success.recycle();

    if (kuaishou_ad_success_point) {
      click(kuaishou_ad_success_point.x, kuaishou_ad_success_point.y);
      sleep(2000);

      var kuaishou_ad_continue = images.read("./kuaishou/kuaishou_ad_continue.png");
      var kuaishou_ad_continue_point = waitForGrayscaleImage(kuaishou_ad_continue, 5000);
      kuaishou_ad_continue.recycle();

      if (kuaishou_ad_continue_point) {
        click(kuaishou_ad_continue_point.x, kuaishou_ad_continue_point.y);
        sleep(2000);
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

function main() {
  while (true) {
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
        kuaishou_ad(); // 点击广告
      }
    } else {
      log("结束领取广告福利");
      break;
    }

    sleep(1000);
  }
}

if (!requestScreenCapture()) {
  toast("请求截图权限失败");
  exit();
}

const x = 1080;
const y = 2340;

const startTime = Date.now();
const timeout = 150 * 60 * 1000;

main();
