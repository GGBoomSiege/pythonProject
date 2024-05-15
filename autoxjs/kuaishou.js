function sign() {
  // 点击去赚钱
  var earnX = (687 + 825) / 2;
  var earnY = (2203 + 2257) / 2;
  click(earnX, earnY);
  sleep(10000);

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  // 导入签到图片
  var sign = images.read("./kuaishou/kuaishou_sign.png");

  var img = captureScreen();
  var result = findImage(img, sign);
  log(result);

  // 执行签到操作，并返回
  if (result === null) {
    var backX = (62 + 154) / 2;
    var backY = (2203 + 2257) / 2;
    click(backX, backY);
  } else {
    click(result.x, result.y);
    sleep(3000);
    var backX = (62 + 154) / 2;
    var backY = (2203 + 2257) / 2;
    click(backX, backY);
  }

  sign.recycle();
  img.recycle();
}

function kuaishou() {
  var x = device.width;
  var y = device.height;

  /*循环定时器1*/
  var interval = setInterval(function () {
    // 执行滑动操作
    swipe((x * (random(8, 10) / 10)) / 3, (y * 2 * (random(11, 13) / 10)) / 3, (x * 2 * (random(8, 10) / 10)) / 3, (y * (random(8, 10) / 10)) / 3, 500);
    sleep(500);
    back();
    sleep(500);
    // 判断是否有多余图片
    var sign = images.read("./kuaishou/kuaishou_cancle.png");
    var img = captureScreen();
    var result = findImage(img, sign);
    if (!(result === null)) {
      click(result.x + 27, result.y + 21);
    }
    sign.recycle();
    img.recycle();
    sleep(500);

    // 判断是否切换其他应用
    var current = currentPackage();
    // toastLog(current);
    if (!(current == "com.kuaishou.nebula")) {
      home();
      sleep(1000);
      app.launch("com.kuaishou.nebula");
    }
    sleep(10 * 1000);
    click(756, 2230);
    sleep(1000);

    if (!requestScreenCapture()) {
      toast("请求截图失败");
      exit();
    }

    // 导入宝箱图片
    var sign = images.read("./kuaishou/kuaishou_baoxiang.png");

    var img = captureScreen();
    var result = findImage(img, sign);
    log(result);

    // 点击宝箱，并返回
    if (result === null) {
      var backX = (62 + 154) / 2;
      var backY = (2203 + 2257) / 2;
      click(backX, backY);
    } else {
      click(result.x, result.y);
      sleep(1000);
      click(990, 410);
      sleep(1000);
      var backX = (62 + 154) / 2;
      var backY = (2203 + 2257) / 2;
      click(backX, backY);
    }

    sign.recycle();
    img.recycle();
  }, 15 * 1000);

  //200min后取消循环
  setTimeout(function () {
    //单次定时器
    clearInterval(interval); //清除循环定时器id1
    openAppSetting("com.kuaishou.nebula");
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
  app.launch("com.kuaishou.nebula");
  waitForPackage("com.kuaishou.nebula");
  // waitForActivity("com.yxcorp.gifshow.HomeActivity");
  sleep(3000);
  sign();
  kuaishou();
}

main();
