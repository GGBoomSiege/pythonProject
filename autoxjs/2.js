const x = 1080;
const y = 2340;

while (true) {
  sleep(20000);
  swipe((2 / 3) * x, (3 / 4) * y, (2 / 3) * x, (1 / 4) * y, 1000);
}
