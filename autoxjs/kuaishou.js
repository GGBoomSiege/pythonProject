// 定义一个函数来等待图片出现 (普通图片)
function waitForImage(image, timeout, threshold) {
  threshold = threshold || 0.9;
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image, {
      threshold: threshold,
    });
    log(found);
    if (found) {
      screenshot.recycle();
      return found;
    }
    if (Date.now() - startTime > timeout) {
      log("等待超时");
      screenshot.recycle();
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

function sign() {
  // 点击去赚钱
  click(756, 2230);

  // 导入签到图片
  var sign = images.read("./kuaishou/kuaishou_sign.png");
  var result = waitForImage(sign, 10000);
  sign.recycle();

  // 执行签到操作，并返回
  if (result) {
    click(result.x, result.y);
    sleep(3000);
    click(108, 2230);
  } else {
    var sign = images.read("./kuaishou/kuaishou_new_sign.png");
    var result = waitForImage(sign, 5000);
    sign.recycle();

    if (result) {
      click(542, 1542);
      sleep(3000);
      click(108, 2230);
    } else {
      click(108, 2230);
    }
  }
}

function kuaishou() {
  // 执行滑动操作
  swipe((x * (random(8, 10) / 10)) / 3, (y * 2 * (random(11, 13) / 10)) / 3, (x * 2 * (random(8, 10) / 10)) / 3, (y * (random(8, 10) / 10)) / 3, 500);
  sleep(1000);
  back();

  // 判断是否有多余图片
  var sign = images.read("./kuaishou/kuaishou_cancle.png");
  var result = waitForImage(sign, 2000);
  sign.recycle();
  if (result) {
    click(result.x + 27, result.y + 21);
  }

  // 判断是否切换其他应用
  if (!(currentPackage() === "com.kuaishou.nebula")) {
    runMain();
  }
  sleep(10 * 1000);

  click(756, 2230);
  sleep(1000);

  // 判断是否有多余图片
  var sign = images.read("./kuaishou/kuaishou_cancle.png");
  var result = waitForImage(sign, 2000);
  sign.recycle();

  if (result) {
    click(result.x + 27, result.y + 21);
  }

  sleep(1000);
  // 滑动页面寻找广告区
  while (true) {
    var kuaishou_ad_flag = images.read("./kuaishou/kuaishou_ad_flag.png");
    var kuaishou_ad_flag_point = waitForImage(kuaishou_ad_flag, 1000);
    kuaishou_ad_flag.recycle();

    if (kuaishou_ad_flag_point) {
      break;
    } else {
      swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 3) * y, 500);
    }
  }

  // 导入宝箱图片
  var sign = images.read("./kuaishou/kuaishou_baoxiang.png");
  var result = waitForImage(sign, 2000);
  sign.recycle();

  // 点击宝箱
  if (result) {
    click(result.x, result.y);
    sleep(1000);
    click(532, 1496);
    sleep(1000);
    kuaishou_ad();
  }
}

//   看广告赚金币
function kuaishou_ad() {
  //   判断是否看完
  var count = 0;
  while (count < 3) {
    // 判断是否观看完成
    var kuaishou_ad_success = images.read("./kuaishou/kuaishou_ad_success.png");
    var kuaishou_ad_success_point = waitForGrayscaleImage(kuaishou_ad_success, 40000, 0.8);
    kuaishou_ad_success.recycle();
    if (kuaishou_ad_success_point) {
      click(kuaishou_ad_success_point.x, kuaishou_ad_success_point.y);
      sleep(2000);

      // 判断是否有继续标识
      var kuaishou_ad_continue = images.read("./kuaishou/kuaishou_ad_continue.png");
      var kuaishou_ad_continue_point = waitForImage(kuaishou_ad_continue, 5000, 0.8);
      kuaishou_ad_continue.recycle();
      if (kuaishou_ad_continue_point) {
        click(kuaishou_ad_continue_point.x, kuaishou_ad_continue_point.y);
      }
      sleep(2000);
    }

    // 判断是否完成
    var kuaishou_ad_flag = images.read("./kuaishou/kuaishou_ad_flag.png");
    var kuaishou_ad_flag_point = waitForImage(kuaishou_ad_flag, 5000, 0.8);
    kuaishou_ad_flag.recycle();
    if (kuaishou_ad_flag_point) {
      break;
    }
    count++;
  }
}

function executeAndWait() {
  kuaishou();

  var kuaishou_ad_flag = images.read("./kuaishou/kuaishou_ad_flag.png");
  var kuaishou_ad_flag_point = waitForImage(kuaishou_ad_flag, 3000);
  kuaishou_ad_flag.recycle();

  if (kuaishou_ad_flag_point) {
    var kuaishou_ad_img = images.read("./kuaishou/kuaishou_ad.png");
    var kuaishou_ad_point = waitForRegionImage(kuaishou_ad_img, kuaishou_ad_flag_point.x, kuaishou_ad_flag_point.y, 944, 106, 3000);
    kuaishou_ad_img.recycle();

    if (kuaishou_ad_point) {
      click(kuaishou_ad_point.x, kuaishou_ad_point.y);
      sleep(5000);
      kuaishou_ad(); // 点击广告
    }
  }

  while (true) {
    var kuaishou_flag = images.read("./kuaishou/kuaishou_flag.png");
    var kuaishou_flag_result = waitForImage(kuaishou_flag, 1000);
    kuaishou_flag.recycle();

    if (kuaishou_flag_result) {
      break;
    } else {
      swipe((2 / 3) * x, (1 / 3) * y, (2 / 3) * x, (2 / 3) * y, 500);
    }
  }

  click(108, 2230);
  sleep(1000);
}

function backMain() {
  openAppSetting("com.kuaishou.nebula");
  sleep(1000);
  id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
  sleep(1000);
  click("确定");
  sleep(1000);
  back();
}

function runMain() {
  app.launch("com.kuaishou.nebula");
  waitForPackage("com.kuaishou.nebula");
  // waitForActivity("com.yxcorp.gifshow.HomeActivity");
  sleep(3000);
  back();
}

// 需要三次启动
function main() {
  device.wakeUp();
  auto.waitFor();

  sleep(5000);
  runMain();
  sleep(5000);
  backMain();

  sleep(5000);
  runMain();
  sleep(5000);
  backMain();

  sleep(5000);
  runMain();

  sleep(5000);
  log("开始执行快手脚本");
  sign();

  sleep(2000);
  while (Date.now() - startTime < timeout) {
    executeAndWait();
  }

  log("结束执行快手脚本，运行时间为 " + (Date.now() - startTime) / 1000 + " 秒。");
  backMain();
}

if (!requestScreenCapture()) {
  toast("请求截图权限失败");
  exit();
}

const x = device.width;
const y = device.height;

const startTime = Date.now();
const timeout = 210 * 60 * 1000;

main();
