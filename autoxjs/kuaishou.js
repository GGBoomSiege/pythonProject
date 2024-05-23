// 定义一个函数来等待图片出现 (普通图片)
function waitForImage(image, timeout) {
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image);
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

function sign() {
  // 点击去赚钱
  click(756, 2230);
  sleep(10000);

  if (!requestScreenCapture()) {
    toast("请求截图失败");
    exit();
  }

  // 导入签到图片
  var sign = images.read("./kuaishou/kuaishou_sign.png");
  var result = waitForImage(sign, 5000);
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
  var x = device.width;
  var y = device.height;

  /*循环定时器1*/
  var interval = setInterval(function () {
    // 执行滑动操作
    swipe((x * (random(8, 10) / 10)) / 3, (y * 2 * (random(11, 13) / 10)) / 3, (x * 2 * (random(8, 10) / 10)) / 3, (y * (random(8, 10) / 10)) / 3, 500);
    sleep(1000);
    back();
    sleep(8 * 1000);
    // 判断是否有多余图片
    var sign = images.read("./kuaishou/kuaishou_cancle.png");
    var result = waitForImage(sign, 2000);
    sign.recycle();
    if (result) {
      click(result.x + 27, result.y + 21);
    }

    // 判断是否切换其他应用
    var current = currentPackage();
    // toastLog(current);
    if (!(current == "com.kuaishou.nebula")) {
      home();
      sleep(1000);
      runMain();
      sleep(1000);
    }
    click(756, 2230);
    sleep(1000);

    if (!requestScreenCapture()) {
      toast("请求截图失败");
      exit();
    }

    // 判断是否有多余图片
    var sign = images.read("./kuaishou/kuaishou_cancle.png");
    var result = waitForImage(sign, 2000);
    sign.recycle();

    if (result) {
      click(result.x + 27, result.y + 21);
    }

    // 导入宝箱图片
    var sign = images.read("./kuaishou/kuaishou_baoxiang.png");
    var result = waitForImage(sign, 2000);
    sign.recycle();

    // 点击宝箱，并返回
    if (result) {
      click(result.x, result.y);
      sleep(1000);
      click(990, 410);
      sleep(1000);
      var backX = (62 + 154) / 2;
      var backY = (2203 + 2257) / 2;
      click(backX, backY);
    } else {
      var backX = (62 + 154) / 2;
      var backY = (2203 + 2257) / 2;
      click(backX, backY);
    }
  }, 25 * 1000);

  //200min后取消循环
  setTimeout(function () {
    //单次定时器
    clearInterval(interval); //清除循环定时器id1
    backMain();
  }, 210 * 60 * 1000);
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

  log("开始执行快手脚本", new Date().toLocaleString());
  sign();
  kuaishou();
  log("结束执行快手脚本", new Date().toLocaleString());
}

main();
