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
function douyin_ad() {
  log("开始广告");
  //   判断是否看完
  let count = 0;
  while (count < 10) {
    // 判断是否跳入直播
    if (count > 2) {
      sleep(1000);
      back();

      // 判断是否完成
      let douyin_ad_complete = images.read("./douyin/douyin_ad_complete.png");
      let douyin_ad_complete_point = waitForImage(douyin_ad_complete, 3000, 0.7);
      douyin_ad_complete.recycle();
      if (douyin_ad_complete_point) {
        click(douyin_ad_complete_point.x, douyin_ad_complete_point.y);
        sleep(1000);
        break;
      }

      let douyin_ad_finish = images.read("./douyin/douyin_ad_finish.png");
      let douyin_ad_finish_point = waitForImage(douyin_ad_finish, 3000, 0.7);
      douyin_ad_finish.recycle();
      if (douyin_ad_finish_point) {
        break;
      }

      // 判断是否中断
      let douyin_ad_continue_flag = images.read("./douyin/douyin_ad_continue_flag.png");
      let douyin_ad_continue_flag_point = waitForImage(douyin_ad_continue_flag, 3000, 0.8);
      douyin_ad_continue_flag.recycle();
      if (douyin_ad_continue_flag_point) {
        click(douyin_ad_continue_flag_point.x, douyin_ad_continue_flag_point.y);
      }
    }

    // 判断是否跳转进下载页
    var douyin_ad_download_cancle = images.read("./douyin/douyin_ad_download_cancle.png");
    var douyin_ad_download_cancle_point = waitForImage(douyin_ad_download_cancle, 30000, 0.7);
    douyin_ad_download_cancle.recycle();
    if (douyin_ad_download_cancle_point) {
      click(douyin_ad_download_cancle_point.x, douyin_ad_download_cancle_point.y);
    }

    // 判断是否观看完成
    var douyin_ad_success = images.read("./douyin/douyin_ad_success.png");
    var douyin_ad_success_point = waitForGrayscaleImage(douyin_ad_success, 3000, 0.7);
    douyin_ad_success.recycle();
    if (douyin_ad_success_point) {
      click(douyin_ad_success_point.x, douyin_ad_success_point.y);
      sleep(2000);

      // 判断是否有继续标识
      var douyin_ad_continue = images.read("./douyin/douyin_ad_continue.png");
      var douyin_ad_continue_point = waitForImage(douyin_ad_continue, 3000, 0.7);
      douyin_ad_continue.recycle();
      if (douyin_ad_continue_point) {
        click(douyin_ad_continue_point.x, douyin_ad_continue_point.y);
      }
      sleep(2000);
    }
    // 判断是否完成
    var douyin_ad_complete = images.read("./douyin/douyin_ad_complete.png");
    var douyin_ad_complete_point = waitForImage(douyin_ad_complete, 3000, 0.7);
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
  log("结束广告");
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

// 每日签到
function douyinSign() {
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
    click(540, 1700);
    sleep(2000);
    douyin_ad();

    // // 判断是否有广告
    // var douyin_sign_ad = images.read("./douyin/douyin_sign_ad.png");
    // var douyin_sign_ad_result = waitForImage(douyin_sign_ad, 10000);
    // douyin_sign_ad.recycle();

    // if (douyin_sign_ad_result) {
    //   click(douyin_sign_ad_result.x, douyin_sign_ad_result.y);
    //   sleep(5000);
    //   douyin_ad(); // 点击广告
    // }
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
      sleep(2000);
      douyin_ad();

      // // 判断是否有广告
      // var douyin_sign_ad = images.read("./douyin/douyin_sign_ad.png");
      // var douyin_sign_ad_result = waitForImage(douyin_sign_ad, 10000);
      // douyin_sign_ad.recycle();

      // if (douyin_sign_ad_result) {
      //   click(douyin_sign_ad_result.x, douyin_sign_ad_result.y);
      //   sleep(5000);
      //   douyin_ad(); // 点击广告
      // }
    } else {
      back();
    }
  }
}

// 积分签到
function douyinPoints() {
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

function kuaishouSign() {
  // 点击去赚钱
  click(756, 2230);

  // 导入签到图片
  var sign = images.read("./kuaishou/kuaishou_sign.png");
  var result = waitForImage(sign, 10000);
  sign.recycle();

  // 执行签到操作，并返回
  if (result) {
    click(result.x, result.y);
  } else {
    var sign = images.read("./kuaishou/kuaishou_new_sign.png");
    var result = waitForImage(sign, 5000);
    sign.recycle();

    if (result) {
      click(542, 1542);
      sleep(2000);
    }
  }

  swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 2) * y, 500);
  sleep(1000);

  var kuaishou_yuyue = images.read("./kuaishou/kuaishou_yuyue.png");
  var kuaishou_yuyue_point = waitForImage(kuaishou_yuyue, 5000);
  kuaishou_yuyue.recycle();

  if (kuaishou_yuyue_point) {
    var kuaishou_yuyue_flag = images.read("./kuaishou/kuaishou_yuyue_flag.png");
    var kuaishou_yuyue_flag_point = waitForRegionImage(kuaishou_yuyue_flag, kuaishou_yuyue_point.x, kuaishou_yuyue_point.y, 970, 148, 3000);
    kuaishou_yuyue_flag.recycle();

    if (kuaishou_yuyue_flag_point) {
      click(kuaishou_yuyue_flag_point.x, kuaishou_yuyue_flag_point.y);

      var kuaishou_yuyue_wards = images.read("./kuaishou/kuaishou_yuyue_wards.png");
      var kuaishou_yuyue_wards_point = waitForImage(kuaishou_yuyue_wards, 5000);
      kuaishou_yuyue_wards.recycle();

      if (kuaishou_yuyue_wards_point) {
        click(kuaishou_yuyue_wards_point.x, kuaishou_yuyue_wards_point.y);
        sleep(5000);

        var kuaishou_yuyue_getwards = images.read("./kuaishou/kuaishou_yuyue_getwards.png");
        var kuaishou_yuyue_getwards_point = waitForImage(kuaishou_yuyue_getwards, 5000);
        kuaishou_yuyue_getwards.recycle();

        if (kuaishou_yuyue_getwards_point) {
          click(kuaishou_yuyue_getwards_point.x, kuaishou_yuyue_getwards_point.y);
          sleep(10000);
          click(535, 1508);
          sleep(5000);
          back();
        }
      }
    }
  }

  swipe((2 / 3) * x, (1 / 3) * y, (2 / 3) * x, (2 / 3) * y, 500);
}

function douyin() {
  runMain("com.ss.android.ugc.aweme.lite");

  // 点击赚钱
  click(542, 2215);
  sleep(3000);
  back();
  sleep(3000);
  click(542, 2215);
  sleep(10000);

  // 关闭抖音
  backMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);

  // 运行抖音
  runMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);
  backMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);

  runMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);
  douyinPoints();
  sleep(2000);
  backMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);

  runMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);
  douyinSign();
  sleep(2000);
  backMain("com.ss.android.ugc.aweme.lite");
  sleep(2000);
}

function kuaishou() {
  runMain("com.kuaishou.nebula");
  sleep(5000);
  backMain("com.kuaishou.nebula");

  sleep(5000);
  runMain("com.kuaishou.nebula");
  sleep(5000);
  backMain("com.kuaishou.nebula");

  sleep(5000);
  runMain("com.kuaishou.nebula");
  sleep(5000);
  kuaishouSign();
  sleep(5000);
  backMain("com.kuaishou.nebula");
}

function main() {
  while (Date.now() - startTime < timeout) {
    log("已运行时间为 " + (Date.now() - startTime) / 1000 + " 秒。");
    log("开始执行抖音脚本");
    // 运行抖音
    douyin();

    log("开始执行快手脚本");
    // 运行快手
    kuaishou();
  }

  log("结束执行脚本，运行时间为 " + (Date.now() - startTime) / 1000 + " 秒。");
}

if (!requestScreenCapture()) {
  toast("请求截图权限失败");
  exit();
}

const x = 1080;
const y = 2340;

const startTime = Date.now();
const timeout = 30 * 60 * 1000;

device.wakeUp();
auto.waitFor();
main();
