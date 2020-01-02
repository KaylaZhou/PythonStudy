function n_1() {
  let all = "";
  for (let a = 1; a < 10; a++) {
    n_2(a);
  }

  function n_2(num) {
    for (let b = 1; b < 10; b++) {
      let str = num + "*" + b + "=" + num * b + " ";
      if (b == num) {
        str = str + "\n";
      }
      if (num < b) {
      } else {
        all = all + str;
      }
    }
  }
}
// n_1();
