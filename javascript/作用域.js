// *函数内可以调用变量, 函数外不能调用变量--(局部变量)
// 例子1:
// function number() {
//   let carName = "hallo word!";
//   console.log("carName111", carName);
// }

// number();

// 例子2:
// function number() {
//   let carName = "hallo word!";
// }

// console.log("carName111", carName);

// number();

// 例子3:
// function aaaa1(params) {
//   let sss = "zhou";
//   console.log(sss);
// }

// function aaaa2(params) {
//   let sss = "mei";
//   console.log(sss);
// }

// aaaa1();

// aaaa2();

// *函数外可以调用变量,变量在函数外定义--(全局变量)
// 例子1:
// let aaa = "kayla";
// console.log(aaa);

// function bbb(params) {
//   let bbb = 1234;
//   console.log(bbb);
// }
// bbb();

// 注:变量不能调用执行, 函数可以调用执行;

// function asdasd(params) {
//   carName = "123123";
// }
// asdasd();
// console.log(carName);

// 例子2: 函数外可以调用变量;
// nnn();
// function nnn() {
//   number = "520";
//   console.log(number);
// }

// 总结: 局部变量(只能在函数内调用变量);全局变量(在函数外调用变量, 如果没有let声明变量, 也可以在函数外调用变量);
