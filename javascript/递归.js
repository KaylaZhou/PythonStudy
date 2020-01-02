let a = 0;

function printName() {
  //
  console.log("周蕊", a);
  //
  a = a + 1;
  if (a < 10) {
    printName();
  }
}

printName();
