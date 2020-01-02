let time = 23;
let time2 = 23;
let x;
if (time < 20) {
  if (time < time2) {
    x = "去跪地板";
  } else {
    x = "晚安!";
  }
} else {
  x = "起来嗨!";
}
// console.log(x);

time < 24 ? (time < time2 ? (x = "去跪地板") : (x = "晚安!")) : (x = "起来嗨!");

console.log(x);
