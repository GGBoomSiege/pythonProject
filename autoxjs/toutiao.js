function sign() {
  // 点击赚钱
  click(449.5, 2218.5);
  sleep(6000);

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  // 导入签到图片
  var sign = images.read("./toutiao/toutiao_sign.png");

  var img = captureScreen();
  var result = findImage(img, sign);
  // log(result);

  // 执行签到操作，并返回
  if (result === null) {
    click(89.5, 2218.5);
  } else {
    click(result.x, result.y);
    sleep(3000);
    click(89.5, 2218.5);
  }

  sign.recycle();
  img.recycle();
}

function toutiao() {
  var x = device.width;
  var y = device.height;

  /*循环定时器1*/
  var interval = setInterval(function () {
    // 执行滑动操作
    swipe((x * (random(8, 10) / 10)) / 3, (y * 2 * (random(11, 13) / 10)) / 3, (x * 2 * (random(8, 10) / 10)) / 3, (y * (random(8, 10) / 10)) / 3, 500);
    sleep(500);
    back();
    // 判断是否切换其他应用
    var current = currentPackage();
    // toastLog(current);
    if (!(current == "com.ss.android.article.lite")) {
      home();
      sleep(1000);
      app.launch("com.ss.android.article.lite");
    }
    sleep(random(8, 10) * 1000);

    // 点击赚钱
    click(449.5, 2218.5);
    sleep(1000);

    if (!requestScreenCapture()) {
      toast("请求截图失败");
      exit();
    }

    // 导入宝箱图片
    var sign = images.read("./toutiao/toutiao_baoxiang.png");

    var img = captureScreen();
    var result = findImage(img, sign);
    // log(result);

    // 判断是否有宝箱
    if (result === null) {
      click(89.5, 2218.5);
    } else {
      click(result.x, result.y);
      sign.recycle();
      img.recycle();
      sleep(3000);

      // 点击取消按钮
      var sign = images.read("./toutiao/cancle.png");
      var img = captureScreen();
      var result = findImage(img, sign);
      if (!(result === null)) {
        click(result.x + 30, result.y + 28);
        sleep(1000);
      }

      click(89.5, 2218.5);
    }

    sign.recycle();
    img.recycle();
  }, 20 * 1000);

  //200min后取消循环
  setTimeout(function () {
    //单次定时器
    clearInterval(interval); //清除循环定时器id1

    sleep(1000);
    // 领取金币
    click(449.5, 2218.5);
    sleep(1000);

    if (!requestScreenCapture()) {
      toast("请求截图失败");
      exit();
    }

    // 导入领取金币图片
    swipe(720, 1560, 720, 780, 500);
    sleep(1000);

    var sign = images.read("./toutiao/toutiao_collectCoins.png");

    var img = captureScreen();
    var result = images.matchTemplate(img, sign, { max: 10 });

    if (!(result === null)) {
      for (var i = 0, len = result["matches"].length; i < len; i++) {
        click(result["matches"][i].point.x, result["matches"][i].point.y);
        sleep(1000);
        click(537, 1313);
        sleep(1000);
      }
    }

    swipe(151, 1224, 812, 1219, 500);
    sleep(1000);
    img = captureScreen();
    result = images.matchTemplate(img, sign, { max: 10 });

    if (!(result === null)) {
      for (var i = 0, len = result["matches"].length; i < len; i++) {
        click(result["matches"][i].point.x, result["matches"][i].point.y);
        sleep(1000);
        click(537, 1313);
        sleep(1000);
      }
    }

    sign.recycle();
    img.recycle();

    openAppSetting("com.ss.android.article.lite");
    sleep(1000);
    id("action_menu_item_child_text").className("android.widget.TextView").text("结束运行").findOne().parent().click();
    sleep(1000);
    click("确定");
    home();
  }, 210 * 60 * 1000);
}

function main() {
  device.wakeUp();
  sleep(2000);
  app.launch("com.ss.android.article.lite");
  waitForPackage("com.ss.android.article.lite");
  waitForActivity("com.ss.android.article.lite.activity.SplashActivity");
  sign();
  toutiao();
}

main();
