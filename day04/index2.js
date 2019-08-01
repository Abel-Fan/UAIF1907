/*

函数语法：
定义函数：
(2)
let fun = new Function('a','b','alert(a+b)')
(3) 字面量的方式
let fun2 = function(参数){函数体}
function(){} //匿名函数
调用方式：
(1)
函数名()
(2)
变量名()
(3)自调用
(function(形参){})(实参)

*/
// let fun2 = function(a,b){
//     alert(a+b)
// }
// fun2(10,30)

// (function(a,b){alert(a+b)})(40,40)

// 参数注意
// 保持一一对应
// 如果形参数量多余实参，多出的形参为undefined
// 入宫实参数量多余形参，多处的实参从arguments对象中找
// rest参数用法

// function add(...arr){
//     let sum = 0
//     for(let i=0;i<arr.length;i++){
//         sum+=arr[i]
//     }
//     console.log(sum)
// }
// add(10,30,50,70)