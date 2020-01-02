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
