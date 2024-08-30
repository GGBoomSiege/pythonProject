const x = 1080;
const y = 2340;

while (true) {
  sleep(1000);
  swipe((2 / 3) * x, (2 / 3) * y, (2 / 3) * x, (1 / 2) * y, 500);
}
