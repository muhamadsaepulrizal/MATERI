// membuat object

// cara 1 function declaration
// function halo() {
//   console.log(this);
//   console.log("hallo");
// }
// this.halo();

// cara 2 object literal
// var obj = {nama:"koko"};
// obj.halo = function () {
//   console.log(this);
//   console.log("hallo");
// };
// obj.halo();

// cara 3 constructor
function Halo() {
  console.log(this);
  console.log("hallo");
}
var obj1 = new Halo();
var obj2 = new Halo();

// konsep this
// console.log(this);
