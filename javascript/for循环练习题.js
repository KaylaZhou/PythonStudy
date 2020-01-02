function jiu() {
  let xxx = "";

  for (let a = 1; a < 10; a = a + 1) {
    // console.log("......a..", a);
    for (let b = 1; b < 10; b = b + 1) {
      // console.log(b);
      let str = a + "*" + b + "=" + a * b + " ";
      if (b == a) {
        str = str + "\n";
      }
      if (a < b) {
        //no
        break;
      } else {
        xxx = xxx + str;
      }
    }
  }
  console.log(xxx);
}
// jiu();

function aaa() {
  let bbb = "";
  for (let i = 1; i < 10; i = i + 1) {
    for (let j = 1; j < 10; j = j + 1) {
      let str = i + "*" + j + "=" + i * j + " ";

      if (j == i) {
        str = str + "\n";
      }
      if (i < j) {
        break;
      }
      bbb = bbb + str;
    }
  }
  console.log(bbb);
}

// aaa();

function nn() {
  let all = "";
  for (let a = 1; a < 10; a++) {
    // console.log(a);
    for (let b = 1; b < 10; b++) {
      // console.log(b);
      let str = a + "x" + b + "=" + a * b + " ";
      if (b == a) {
        str = str + "\n";
      }
      if (a < b) {
        break;
      }
      all = all + str;
    }
  }
  console.log(all);
}
// nn();

// 工资超过1000的部分, 需要缴纳个税(税率3%), 根据用户输入的工资金额, 计算税后工资;

function name() {
  let m = "请输入工资:";
  if (m > 1000) {
    m = m - (m - 1000) * 0.03;
    console.log("税后工资" + m);
  } else {
    console.log("税后工资" + m);
  }
  // console.log(m);
}

name();
