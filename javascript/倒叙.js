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
let all = "";

let a = 1;
function fn_a() {
  nin();
  a++;
  if (a < 10) {
    fn_a();
  }
}
fn_a();

console.log(all);

function nin() {
  let b = 1;
  function fn_b() {
    //
    let str = a + "*" + b + "=" + a * b + " ";
    if (b == a) {
      str = str + "\n";
    }
    if (a < b) {
      // break;
    } else {
      all = all + str;
    }
    //
    b++;
    if (b < 10) {
      fn_b();
    }
  }
  fn_b();
}
