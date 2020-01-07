// function jiu() {
//   let xxx = "";

//   for (let a = 1; a < 10; a = a + 1) {
//     // console.log("......a..", a);
//     for (let b = 1; b < 10; b = b + 1) {
//       // console.log(b);
//       let str = a + "*" + b + "=" + a * b + " ";
//       if (b == a) {
//         str = str + "\n";
//       }
//       if (a < b) {
//         //no
//         break;
//       } else {
//         xxx = xxx + str;
//       }
//     }
//   }
//   console.log(xxx);
// }
// jiu();

// function aaa() {
//   let bbb = "";
//   for (let i = 1; i < 10; i = i + 1) {
//     for (let j = 1; j < 10; j = j + 1) {
//       let str = i + "*" + j + "=" + i * j + " ";

//       if (j == i) {
//         str = str + "\n";
//       }
//       if (i < j) {
//         break;
//       }
//       bbb = bbb + str;
//     }
//   }
//   console.log(bbb);
// }

// aaa();

// function nn() {
//   let all = "";
//   for (let a = 1; a < 10; a++) {
//     // console.log(a);
//     for (let b = 1; b < 10; b++) {
//       // console.log(b);
//       let str = a + "x" + b + "=" + a * b + " ";
//       if (b == a) {
//         str = str + "\n";
//       }
//       if (a < b) {
//         break;
//       }
//       all = all + str;
//     }
//   }
//   console.log(all);
// }
// nn();

function name() {
  for (let a = 0; a <= 20; a++) {
    console.log("...a", a);
    for (let b = 0; b <= 10; b++) {
      console.log("...b", b);
      for (let c = 0; c <= 4; c++) {
        // console.log("...c.", c);

        if (a + 2 * b + 5 * c == 20) {
          console.log("一块:", a, "两块:" + b + "五块:" + c + "+");
        }
      }
    }
  }
}
// name();

for (let i = 100; i < 1000; i++) {
  let a = parseInt(i % 10);
  let b = parseInt((i / 10) % 10);
  let c = parseInt(i / 100);
  if (a * a * a + b * b * b + c * c * c == i) {
    console.log("水仙花数:", i + i + "\n");
  }
}
