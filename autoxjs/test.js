// "ui";
// ui.layout(
//   <vertical h="100dp">
//     <text layout_weight="1" text="控件1" bg="#ff0000" />
//     <text layout_weight="1" text="控件2" bg="#00ff00" />
//     <text layout_weight="1" text="控件3" bg="#0000ff" />
//   </vertical>
// );

// home();

// if (text("文件").findOne(3000)) {
//   log("已经找到了");
// } else {
//   log("没有找到");
// }

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

function temp() {
  // app.launch("io.cpen.mobile");
  // waitForPackage("com.google.android.googlequicksearchbox");
  // log("1");
  // className("android.view.View").desc("@cPenCoreTeam").waitFor();
  // log("3");
  var path1 = files.cwd();
  log(path1);
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
  var startup = images.clip(img, 514, 1774, 54, 42);
  images.save(startup, "../Pictures/Screenshots/temp.png");
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

  startup.recycle();
  // img.recycle();
}

// device.wakeUp();
// toast("good job!");
// temp();
readImage();
