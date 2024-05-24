device.wakeUp();
sleep(1000);

// 定义一个函数来等待图片出现 (普通图片)
function waitForImage(image, timeout) {
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image);
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
function waitForGrayscaleImage(image, timeout) {
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(images.grayscale(screenshot), images.grayscale(image));
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

// 定义一个函数来等待图片出现 (区域找图)
function waitForRegionImage(image, x, y, width, height, timeout) {
  var startTime = Date.now();
  while (true) {
    var screenshot = captureScreen();
    var found = images.findImage(screenshot, image, {
      region: [x, y, width, height],
      threshold: 0.9,
    });
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

//   看广告赚金币
function douyin_ad() {
  var douyin_ad = images.read("./douyin/douyin_ad.png");
  var point = waitForImage(douyin_ad, 5000);
  if (point) {
    click(point.x + 765, point.y + 87);
    //   判断是否看完
    while (true) {
      var douyin_ad_success = images.read("./douyin/douyin_ad_success.png");
      var douyin_ad_success_point = waitForGrayscaleImage(douyin_ad_success, 40000);
      if (douyin_ad_success_point) {
        click(douyin_ad_success_point.x, douyin_ad_success_point.y);
        sleep(1000);
        click(540, 1360);
      } else {
        break;
      }
      douyin_ad_success.recycle();
    }
    back();
  }
  douyin_ad.recycle();
}

function test(a, b, threshold) {
  threshold = threshold || 1;

  log(a, b, threshold);
}

function main() {
  //   看广告赚金币
  //   douyin_ad();

  // let douyin_ad_img = images.read("./douyin/douyin_ad.png");
  // //   let point = waitForRegionImage(douyin_ad_img, 819, 1432, 218, 94, 5000);
  // var point = images.findImage(captureScreen(), douyin_ad_img, {
  //   region: [819, 1432, 218, 94],
  //   threshold: 0.9,
  // });
  // log(point);
  test(123, 123, 0.8);
}

main();
