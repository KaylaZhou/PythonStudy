// break()终止循环,例子:

function a() {
  for (let i = 0; i <= 10; i++) {
    if (i == 3) {
      break;
    }
    console.log("该数字为:", i);
  }
}

a();

let m = 0;
function b() {
  for (let i = 0; i <= 10; i = i + 1) {
    console.log("i--- ", i);
    console.log("m--- ", m);
    console.log("*********************");

    if (m == 0) {
      m = m + 1;
    }
  }
}
// b();
