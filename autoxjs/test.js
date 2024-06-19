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

function backMain(app) {
  openAppSetting(app);
  sleep(1000);
  id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
  sleep(1000);
  click("确定");
  sleep(1000);
  back();
}

function douyin_ad() {
  //   判断是否看完
  let count = 0;
  while (count < 4) {
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

function run() {
  let text = ["你好啊", "不好", "很好"];
  let answer = [];
  for (let i in text) {
    sleep(1000);
    toast(text[i]);
  }
}

function runApp() {
  app.launch("com.google.android.googlequicksearchbox");
}

function http() {
  console.time("求和");
  var sum = 0;
  for (let i = 0; i < 100000; i++) {
    sum += i;
  }
  console.timeEnd("求和");
  log(sum);
  // 打印 求和: xxx ms

  alert("运行完成！");
}

function readImage() {
  // app.launch("io.cpen.mobile");
  // waitForPackage("io.cpen.mobile");
  // className("android.view.View").desc("@cPenCoreTeam").waitFor();
  // app.launch("com.ss.android.ugc.aweme.lite");
  // waitForPackage("com.ss.android.ugc.aweme.lite");
  // if (!requestScreenCapture()) {
  //   toast("请求截图失败");
  //   exit();
  // }
  // var img = captureScreen();
  // images.save(img, "./douyin.png");

  // var startup = images.read("./startup.png");
  // var img = images.read("./img.png");
  var img = images.read("../Pictures/Screenshots/123.jpg");

  // 截取小图
  var startup = images.clip(img, 50, 50, 32, 32);
  // 73 82

  images.save(startup, "../Pictures/Screenshots/temp.png");
  // var startup = images.read("./douyin/douyin_ad_flag.png");
  // var img = captureScreen();
  // var startup_point = images.findImage(img, startup);
  startup.recycle();
  img.recycle();

  // var point = images.findImage(img, startup);
  // if (startup_point) {
  //   var startup = images.read("./douyin/douyin_ad.png");
  //   var img = captureScreen();
  //   var found = images.findImage(img, startup, {
  //     region: [startup_point.x, startup_point.y, 870, 194],
  //   });
  //   if (found) {
  //     log(found);
  //   } else {
  //     log("未找到图片found");
  //   }
  // } else {
  //   log("未找到图片startup_point");
  // }

  // if (startup) {
  //   var width = img.getWidth();
  //   var height = img.getHeight();
  //   console.log(width, height);
  // }

  // var img = captureScreen();
  // images.saveImage(img, "./1.png");

  // var result = images.matchTemplate(img, startup, {
  //   threshold: 0.3,
  // }).matches;

  // var result = findImage(img, startup);
  // if (result === null) {
  //   toastLog("未找到指定图片");
  // } else {
  //   toastLog("已找到指定图片,位置为：" + " ( " + (result.x + 152 / 2) + " , " + (result.y + 152 / 2) + " ) ");
  // }

  // toastLog(result.x + 152 / 2);
  // toastLog(result.y + 152 / 2);
  // longClick(result.x + 152 / 2, result.y + 152 / 2);
}

function runMain() {
  app.launch("com.ss.android.ugc.aweme.lite");
  waitForPackage("com.ss.android.ugc.aweme.lite");
  // waitForActivity("com.ss.android.ugc.aweme.main.MainActivity");
  sleep(3000);
  back();
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
  var index_115_result = waitForImage(index_115, 60000);
  index_115.recycle();

  if (index_115_result) {
    click(index_115_result.x, index_115_result.y);

    // 签到
    var sign_115 = images.read("./appStartUp/sign_115.png");
    var sign_115_result = waitForImage(sign_115, 60000);
    sign_115.recycle();

    if (!sign_115_result) {
      click(148, 158);

      var sign_115_flag = images.read("./appStartUp/sign_115_flag.png");
      var sign_115_flag_result = waitForImage(sign_115_flag, 60000);
      sign_115_flag.recycle();

      if (sign_115_flag_result) {
        click(sign_115_flag_result.x, sign_115_flag_result.y);
      }
    }
  }

  sleep(1000);
  backMain("com.ylmf.androidclient");
}

function temp() {
  let douyin_ad_finish = images.read("./douyin/douyin_ad_finish.png");
  let douyin_ad_finish_point = waitForImage(douyin_ad_finish, 3000, 0.7);
  log(douyin_ad_finish_point);
}

function main() {
  device.wakeUp();
  // toast("good job!");
  // temp();
  readImage();
  // if (!(currentPackage() === "com.ss.android.ugc.aweme.lite")) {
  //   runMain();
  // }
}

const x = 1080;
const y = 2340;

// main();
// temp();
// swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 3) * y, 500);

// const startTime = Date.now();
// sleep(2000);
// const endTime = Date.now();

// log(endTime - startTime);

log(currentPackage());
// log(currentActivity());
// click{70, 1650}
// sign_115();
