// 每日签到
function sign() {
  // 点击赚钱
  click(542, 2215);
  sleep(3000);
  back();
  sleep(1500);
  click(542, 2215);
  sleep(3000);

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  var sign = images.read("./douyin/pre_sign.png");

  var img = captureScreen();
  var result = findImage(img, sign);
  sign.recycle();
  img.recycle();

  if (result === null) {
    // 导入签到图片
    var sign = images.read("./douyin/douyin_sign.png");

    var img = captureScreen();
    var result = findImage(img, sign);
    // log(result);

    // 执行签到操作，并返回
    if (result === null) {
      back();
    } else {
      click(result.x, result.y);
      sleep(3000);
      click(540, 1700);
      sleep(3000);
      click(540, 1700);
      sleep(3000);
      back();
    }

    sign.recycle();
    img.recycle();
  } else {
    click(result.x, result.y);
    sleep(3000);
  }
}

// 积分签到
function points() {
  // 点击我
  click(971, 2215);
  sleep(5000);

  click(381, 1070);
  sleep(5000);

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  // 导入积分签到图片
  var sign = images.read("./douyin/douyin_points.png");

  var img = captureScreen();
  var result = findImage(img, sign);
  // toastLog(result);

  // 执行签到操作，并返回
  if (result === null) {
    back();
  } else {
    click(result.x, result.y);
    sleep(5000);
    back();
  }

  sleep(1000);
  back();

  sign.recycle();
  img.recycle();
}

function douyin() {
  var x = device.width;
  var y = device.height;

  /*循环定时器1*/
  var interval = setInterval(function () {
    // 执行滑动操作
    swipe((x * (random(8, 10) / 10)) / 3, (y * 2 * (random(11, 13) / 10)) / 3, (x * 2 * (random(8, 10) / 10)) / 3, (y * (random(8, 10) / 10)) / 3, 500);
    sleep(1000);
    back();
    // 判断是否切换其他应用
    var current = currentPackage();
    // toastLog(current);
    if (!(current == "com.ss.android.ugc.aweme.lite")) {
      home();
      sleep(1000);
      app.launch("com.ss.android.ugc.aweme.lite");
    }
    sleep(10 * 1000);

    // 点击赚钱
    click(542, 2215);
    sleep(1000);

    if (!requestScreenCapture()) {
      toast("请求截图失败");
      exit();
    }

    // 导入宝箱图片
    var sign = images.read("./douyin/douyin_baoxiang.png");

    var img = captureScreen();
    var result = findImage(img, sign);
    // log(result);

    // 点击宝箱，并返回
    if (result === null) {
      back();
    } else {
      click(result.x, result.y);
      sleep(1000);
      back();
      sleep(1000);
      back();
    }

    sign.recycle();
    img.recycle();
  }, 15 * 1000);

  //200min后取消循环
  setTimeout(function () {
    //单次定时器
    clearInterval(interval); //清除循环定时器id1
    openAppSetting("com.ss.android.ugc.aweme.lite");
    sleep(1000);
    id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
    sleep(1000);
    click("确定");
    home();
  }, 210 * 60 * 1000);
}

function backMain() {
  openAppSetting("com.ss.android.ugc.aweme.lite");
  sleep(1000);
  id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
  sleep(1000);
  click("确定");
  home();
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
  sleep(2000);
  log("开始执行抖音脚本", new Date().toLocaleString());
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
  douyin();
  log("结束执行抖音脚本", new Date().toLocaleString());
}

main();