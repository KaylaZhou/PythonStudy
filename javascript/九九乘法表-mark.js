//99乘法表综合应用
function for_99() {
  let all = "";
  for (let a = 1; a < 10; a = a + 1) {
    //fun1
    for (let b = 1; b < 10; b = b + 1) {
      // a * b = a*b
      let str = a + "*" + b + "=" + a * b + " ";
      if (a >= b) {
        if (a == b) {
          str = str + "\n";
        }
        all = all + str;
      }
    }
    // fun1 - end;
  }
  console.log(all);
}

for_99();

//字符串的学习
function str_study() {
  //学习字符串
  let txt = "周abcdefghijk";
  let qp = txt[4]; // 字符串切片. 结果: d
  // console.log(qp);

  let len = txt.length; // 打印字符串长度
  // console.log(len);

  let txt2 = "梅abcdfghijk"; // 反斜杠表示特殊字符
  // console.log(txt2);

  let txt3 = txt + " * " + txt2; //字符串拼接
  // console.log(txt3);

  txt = txt + txt3;
  console.log(txt);
}

// str_study();

//计算 10 以内的加法 1-10的加法
// 1+2+3+4+5+6+7+8+9+10 = ?
function add_add() {
  let num = "";
  for (let i = 1; i <= 10; i = i + 1) {
    num = num + i + " ";
  }
  console.log(num);
}

// add_add();

//比较
function than_x() {
  let a = 2;
  let b = 1;

  let p = a <= b;
  if (p) {
    console.log("mmm");
  } else {
    console.log("xxxx");
  }
}

// than_x();

// function name() {
//   let all = "";

//   for (let a = 1; a < 10; a++) {
//     xxx(a);
//   }

//   function xxx(e) {

//     for (let b = 1; b < 10; b++) {
//       let str = e + "*" + b + "=" + e * b + " ";
//       if (b == e) {
//         str = str + "\n";
//       }
//       if (e < b) {
//         break;
//       }

//       all = all + str;
//     }
//   }
//   console.log(all);
// }

// 递归,乘法表:
// let all = "";

// let a = 1;
// function fn_a() {
//   nin();
//   a++;
//   if (a < 10) {
//     fn_a();
//   }
// }
// fn_a();

// console.log(all);

// function nin() {
//   let b = 1;
//   function fn_b() {
//     //
//     let str = a + "*" + b + "=" + a * b + " ";
//     if (b == a) {
//       str = str + "\n";
//     }
//     if (a < b) {
//       // break;
//     } else {
//       all = all + str;
//     }
//     //
//     b++;
//     if (b < 10) {
//       fn_b();
//     }
//   }
//   // fn_b();
// }
let xx = ""; //声明一个空的变量,用于存储函数二中的式子.
let a = 1;

function a_1() {
  n_n(); //调用函数名,用于函数二中的函数名.

  a++;
  if (a < 10) {
    a_1();
  }
}
a_1();

function n_n() {
  //调用第一个函数
  let b = 1;

  function a_2() {
    let str = a + "*" + b + "=" + a * b + " ";

    if (b == a) {
      str = str + "\n";
    }

    if (a < b) {
      //n
    } else {
      xx = xx + str;
    }

    b++;
    if (b < 10) {
      a_2(); //当b<10时,执行函数a_2()
    }
  }
  a_2(); //调用,启动函数
}

console.log(xx);
