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
  var startup = images.clip(img, 505, 2132, 72, 72);
  // 582 2210

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

function temp() {
  // 进入挖矿页
  var athene_main = images.read("./appStartUp/athene_main.png");
  var athene_main_result = waitForImage(athene_main, 10000);
  athene_main.recycle();

  if (athene_main_result) {
    click(athene_main_result.x, athene_main_result.y);

    // 判断是否开始
    var athene_startup = images.read("./appStartUp/athene_startup.png");
    var athene_startup_result = waitForImage(athene_startup, 10000);
    athene_startup.recycle();

    if (athene_startup_result) {
      click(athene_startup_result.x, athene_startup_result.y);
      sleep(1000);
    }

    // 判断是否领取
    var athene_rewards = images.read("./appStartUp/athene_rewards.png");
    var athene_rewards_result = waitForImage(athene_rewards, 10000);
    athene_rewards.recycle();

    if (athene_rewards_result) {
      click(athene_rewards_result.x, athene_rewards_result.y);
      sleep(1000);
    }

    var athene_main = images.read("./appStartUp/athene_main.png");
    if (!waitForImage(athene_main, 10000)) {
      sleep(1000);
      click(150, 2190);
    }
    athene_main.recycle();
  }

  sleep(1000);
  home();
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

const x = device.width;
const y = device.height;
// main();
temp();

// const startTime = Date.now();
// sleep(2000);
// const endTime = Date.now();

// log(endTime - startTime);

// log(currentPackage());
// log(currentActivity());
// click{70, 1650}
