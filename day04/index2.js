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

// 作用域：变量作用的范围
// 根据作用域不同，把变量分为全局变量,局部变量
// 全局变量：在任何情况下都可以使用的变量
// 局部变量：只能在块或者是函数内使用的称为局部变量

// let aa = 123  //全局变量
// function fun(){
//     // let aa = 456
//     console.log(aa)   // 1 456
//     function fun2(){
//         // let aa = 789
//         console.log(aa) // 2 789
//     }
//     fun2()
// }
// fun()
// console.log(aa)  // 3 123

// 作用域链


// ES5 函数作用域 function(){}
// ES6 块级作用域  {}  ,只有let申明的变量才是块级作用域
// var 6之前

// var aa = 123
// {
//     var aa = 456
// }
// console.log(aa)

// for(let i=0;i<10;i++){
//     console.log(i)
// }
// // 0 1 2 3 4 5 6 7 8 9
// console.log(i)  // 10




//var let 区别
//(1) let 支持块级作用域 var支持函数作用域
//(2) var 支持变量提升(js加载时会经历 预解析（把var申明的变量以及function提前放到内存中）->解析 )
//(3) let会出现暂时性死区

// console.log(aa)
// let aa = 10
// console.log(aa)

// console.log(aa)
// var aa = 10
// console.log(aa)

// aa()
// function aa(){
//     console.log(123)
// }


// let aa = 123
// function fun(){
//     console.log(aa)  // 123  error : aa is not defined
//     let aa = 456
//     console.log(aa)  // 456
// }
// fun()

// 名词解释
// 闭包函数:两个嵌套的函数，内部函数使用外部函数的变量，然后在全局环境下调用内部函数时，形成闭包。用作与保护变量。
function fun1(){
    let aa = []
    function fun2(data){
        aa.push(data)
        console.log(aa)
    }
    return fun2
}
let fun2 = fun1()
fun2(123)
fun2(456)
fun2(789)