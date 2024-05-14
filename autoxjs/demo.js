device.wakeUp();
sleep(1000);

var sign = images.read("./kuaishou/kuaishou_cancle.png");

var img = captureScreen();
var result = findImage(img, sign);

if (!(result === null)) {
  toastLog(result.x + 27);
  toastLog(result.y + 21);
}

// bounds("(48,2180,131,2257)")
// var x = (687 + 825) / 2;
// var y = (2203 + 2257) / 2;
// log(x);
// log(y);

// var x = device.width;
// var y = device.height;
// log((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 3) * y);

// swipe(720, 1560, 720, 780, 500);
// sleep(1000);

// var sign = images.read("./toutiao/toutiao_collectCoins.png");

// var img = captureScreen();
// var result = images.matchTemplate(img, sign, { max: 10 });

// if (!(result === null)) {
//   for (var i = 0, len = result["matches"].length; i < len; i++) {
//     click(result["matches"][i].point.x, result["matches"][i].point.y);
//     sleep(1000);
//     click(537, 1313);
//     sleep(1000);
//   }
// }

// swipe(151, 1224, 812, 1219, 500);
// sleep(1000);
// img = captureScreen();
// result = images.matchTemplate(img, sign, { max: 10 });

// if (!(result === null)) {
//   for (var i = 0, len = result["matches"].length; i < len; i++) {
//     click(result["matches"][i].point.x, result["matches"][i].point.y);
//     sleep(1000);
//     click(537, 1313);
//     sleep(1000);
//   }
// }

// app.launch("com.ss.android.ugc.aweme.lite");
// waitForPackage("com.ss.android.ugc.aweme.lite");
// waitForActivity("com.ss.android.ugc.aweme.main.MainActivity");

// sleep(3000);
// if (!(currentPackage() === "com.ss.android.ugc.aweme.lite")) {
//   home();
//   app.launch("com.ss.android.ugc.aweme.lite");
//   waitForPackage("com.ss.android.ugc.aweme.lite");
//   waitForActivity("com.ss.android.ugc.aweme.main.MainActivity");
// }

// app.launch("com.kuaishou.nebula");
