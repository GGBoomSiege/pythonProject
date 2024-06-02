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

// 每日签到
function sign() {
  // 点击赚钱
  click(542, 2215);
  sleep(3000);
  back();
  sleep(1500);
  click(542, 2215);
  sleep(3000);

  var preSign = images.read("./douyin/pre_sign.png");
  var preResult = waitForImage(preSign, 3000);
  preSign.recycle();

  if (preResult) {
    click(preResult.x, preResult.y);
    sleep(3000);

    // 判断是否有广告
    var douyin_sign_ad = images.read("./douyin/douyin_sign_ad.png");
    var douyin_sign_ad_result = waitForImage(douyin_sign_ad, 10000);
    douyin_sign_ad.recycle();

    if (douyin_sign_ad_result) {
      click(douyin_sign_ad_result.x, douyin_sign_ad_result.y);
      sleep(5000);
      douyin_ad(); // 点击广告
    }
  } else {
    // 导入签到图片
    var sign = images.read("./douyin/douyin_sign.png");
    var result = waitForImage(sign, 3000);
    sign.recycle();

    // 执行签到操作，并返回
    if (result) {
      click(result.x, result.y);
      sleep(3000);
      click(540, 1700);
      sleep(3000);

      // 判断是否有广告
      var douyin_sign_ad = images.read("./douyin/douyin_sign_ad.png");
      var douyin_sign_ad_result = waitForImage(douyin_sign_ad, 10000);
      douyin_sign_ad.recycle();

      if (douyin_sign_ad_result) {
        click(douyin_sign_ad_result.x, douyin_sign_ad_result.y);
        sleep(5000);
        douyin_ad(); // 点击广告
      }
    } else {
      back();
    }
  }
}

// 积分签到
function points() {
  // 点击我
  click(971, 2215);
  sleep(3000);
  click(381, 1070);
  sleep(3000);

  // 导入积分签到图片
  var sign = images.read("./douyin/douyin_points.png");
  var result = waitForImage(sign, 3000);
  sign.recycle();

  // 执行签到操作，并返回
  if (result) {
    click(result.x, result.y);
    sleep(3000);
    back();
  } else {
    back();
  }

  sleep(1000);
  back();
}

function douyin() {
  // 执行滑动操作
  swipe((x * (random(8, 10) / 10)) / 3, (y * 2 * (random(11, 13) / 10)) / 3, (x * 2 * (random(8, 10) / 10)) / 3, (y * (random(8, 10) / 10)) / 3, 500);
  sleep(1000);
  back();

  if (!(currentPackage() === "com.ss.android.ugc.aweme.lite")) {
    runMain();
  }
  sleep(10 * 1000);

  // 点击赚钱
  click(542, 2215);
  sleep(1000);

  sleep(2000);
  // // 滑动页面寻找广告区
  // while (true) {
  //   var douyin_ad_flag = images.read("./douyin/douyin_ad_flag.png");
  //   var douyin_ad_flag_point = waitForImage(douyin_ad_flag, 1000);
  //   douyin_ad_flag.recycle();

  //   if (douyin_ad_flag_point) {
  //     break;
  //   } else {
  //     swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 3) * y, 500);
  //   }
  // }

  swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 3) * y, 500);

  // 导入宝箱图片
  var sign = images.read("./douyin/douyin_baoxiang.png");
  var result = waitForImage(sign, 3000);
  sign.recycle();

  // 点击宝箱
  if (result) {
    click(result.x, result.y);
    sleep(3000);
    click(522, 1598);
    sleep(5000);
    douyin_ad(); // 点击广告
  }

  // back();
}

//   看广告赚金币
function douyin_ad() {
  //   判断是否看完
  let count = 0;
  while (count < 6) {
    // 判断是否跳入直播
    if (count > 2) {
      sleep(1000);
      back();

      // 判断是否完成
      let douyin_ad_complete = images.read("./douyin/douyin_ad_complete.png");
      let douyin_ad_complete_point = waitForImage(douyin_ad_complete, 5000, 0.7);
      douyin_ad_complete.recycle();
      if (douyin_ad_complete_point) {
        click(douyin_ad_complete_point.x, douyin_ad_complete_point.y);
        sleep(1000);
        break;
      }

      // 判断是否中断
      let douyin_ad_continue_flag = images.read("./douyin/douyin_ad_continue_flag.png");
      let douyin_ad_continue_flag_point = waitForImage(douyin_ad_continue_flag, 5000, 0.8);
      douyin_ad_continue_flag.recycle();
      if (douyin_ad_continue_flag_point) {
        click(douyin_ad_continue_flag_point.x, douyin_ad_continue_flag_point.y);
      }
    }

    // 判断是否跳转进下载页
    var douyin_ad_download_cancle = images.read("./douyin/douyin_ad_download_cancle.png");
    var douyin_ad_download_cancle_point = waitForImage(douyin_ad_download_cancle, 40000, 0.7);
    douyin_ad_download_cancle.recycle();
    if (douyin_ad_download_cancle_point) {
      click(douyin_ad_download_cancle_point.x, douyin_ad_download_cancle_point.y);
    }

    // 判断是否观看完成
    var douyin_ad_success = images.read("./douyin/douyin_ad_success.png");
    var douyin_ad_success_point = waitForGrayscaleImage(douyin_ad_success, 5000, 0.7);
    douyin_ad_success.recycle();
    if (douyin_ad_success_point) {
      click(douyin_ad_success_point.x, douyin_ad_success_point.y);
      sleep(2000);

      // 判断是否有继续标识
      var douyin_ad_continue = images.read("./douyin/douyin_ad_continue.png");
      var douyin_ad_continue_point = waitForImage(douyin_ad_continue, 5000, 0.7);
      douyin_ad_continue.recycle();
      if (douyin_ad_continue_point) {
        click(douyin_ad_continue_point.x, douyin_ad_continue_point.y);
      }
      sleep(2000);
    }
    // 判断是否完成
    var douyin_ad_complete = images.read("./douyin/douyin_ad_complete.png");
    var douyin_ad_complete_point = waitForImage(douyin_ad_complete, 5000, 0.7);
    douyin_ad_complete.recycle();
    if (douyin_ad_complete_point) {
      click(douyin_ad_complete_point.x, douyin_ad_complete_point.y);
      sleep(1000);
      break;
    }

    // 判断是否完成
    var douyin_ad_flag = images.read("./douyin/douyin_ad_flag.png");
    var douyin_ad_flag_point = waitForImage(douyin_ad_flag, 3000, 0.7);
    douyin_ad_flag.recycle();
    if (douyin_ad_flag_point) {
      break;
    }

    count++;
  }
}

function executeAndWait() {
  douyin();

  var douyin_ad_flag = images.read("./douyin/douyin_ad_flag.png");
  var douyin_ad_flag_point = waitForImage(douyin_ad_flag, 3000);
  douyin_ad_flag.recycle();

  if (douyin_ad_flag_point) {
    var douyin_ad_img = images.read("./douyin/douyin_ad.png");
    var douyin_ad_point = waitForRegionImage(douyin_ad_img, douyin_ad_flag_point.x, douyin_ad_flag_point.y, 870, 194, 3000);
    douyin_ad_img.recycle();

    if (douyin_ad_point) {
      click(douyin_ad_point.x, douyin_ad_point.y);
      sleep(5000);
      douyin_ad(); // 点击广告
    }
  }

  let count = 0;
  while (count < 4) {
    var douyin_flag = images.read("./douyin/douyin_flag.png");
    var douyin_flag_result = waitForImage(douyin_flag, 1000);
    douyin_flag.recycle();

    if (douyin_flag_result) {
      break;
    } else {
      swipe((2 / 3) * x, (1 / 3) * y, (2 / 3) * x, (2 / 3) * y, 500);
    }

    count++;
  }

  back();
  sleep(1000);
}

function backMain() {
  openAppSetting("com.ss.android.ugc.aweme.lite");
  sleep(1000);
  id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
  sleep(1000);
  click("确定");
  sleep(1000);
  back();
}

function runMain() {
  app.launch("com.ss.android.ugc.aweme.lite");
  waitForPackage("com.ss.android.ugc.aweme.lite");
  // waitForActivity("com.ss.android.ugc.aweme.main.MainActivity");
  sleep(3000);
  back();
}

function main() {
  device.wakeUp();
  auto.waitFor();

  sleep(2000);
  log("开始执行抖音脚本");
  // 运行抖音
  runMain();

  // 点击赚钱
  click(542, 2215);
  sleep(3000);
  back();
  sleep(3000);
  click(542, 2215);
  sleep(10000);

  // 关闭抖音
  backMain();
  sleep(2000);

  // 运行抖音
  runMain();
  sleep(2000);
  backMain();
  sleep(2000);

  runMain();
  sleep(2000);
  points();
  sleep(2000);
  backMain();
  sleep(2000);

  runMain();
  sleep(2000);
  sign();
  sleep(2000);
  backMain();
  sleep(2000);

  runMain();
  sleep(2000);

  while (Date.now() - startTime < timeout) {
    executeAndWait();
  }

  log("结束执行抖音脚本，运行时间为 " + (Date.now() - startTime) / 1000 + " 秒。");
  backMain();
}

if (!requestScreenCapture()) {
  toast("请求截图权限失败");
  exit();
}

const x = device.width;
const y = device.height;

const startTime = Date.now();
const timeout = 150 * 60 * 1000;

main();
