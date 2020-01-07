// 1.先声明一个变量,用于控制递归的次数
// 2.创建函数,并且自调用
// 3;变量自增,达到递归条件
// 4.测试递归是否成立
// 5.建立第二个递归
// 6.在第二个递归中,测试a和b碰面
// 7.拼写式子,并测试式子是否成立
// 8.创建全局变量,存储式子
// 9.测试存储的结果, 是否为一行
// 10.分析测试结果, 设置换行
// 11.设置条件,将需要存储的式子和不需要存储的式子分开
// let all = "";
// function xxx() {
//   for (let a = 9; a >= 1; a--) {
//     // console.log("...a.", a);
//     for (let b = 9; b >= 1; b--) {
//       // console.log(b);
//       let str = a + "*" + b + "=" + a * b + " ";
//       if (b == 1) {
//         str = str + "\n";
//       }
//       if (a < b) {
//       } else {
//         all = all + str;
//       }
//       //     }
//       //   }
//     }
//   }
//   console.log(all);
// }
// xxx();
let all = "";
let a = 9;
function fn1() {
  // console.log("..a", a);
  xxx();
  a = a - 1;
  if (a >= 1) {
    fn1();
  }
}
fn1();

function xxx() {
  let b = 9;
  function fn2() {
    // console.log(b);
    let str = a + "*" + b + "=" + a * b + " ";
    if (b == 1) {
      str = str + "\n";
    }
    if (a < b) {
    } else {
      all = all + str;
    }

    b = b - 1;
    if (b >= 1) {
      fn2();
    }
  }
  fn2();
}
console.log(all);
// xxx();
