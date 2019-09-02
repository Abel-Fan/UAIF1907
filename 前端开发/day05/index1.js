// 函数
// 一、定义：封装一个特定功能的代码块，以便重复调用。
// 二、语法：
// 定义函数
/*
(1)利用function关键字
function aa(){}
(2)字面量的方式
let fn = function(){}
(3)通过Function实例化
let fn = new Function('a','b','c','alert(a+b+c)')
*/
// 调用函数
/*
1、
函数名()
2、
变量名()
3、匿名函数的自导用
(function(){})()
*/

// 参数：
// 分类：  形参：形式参数，定义函数的括号中，接收实参
//        实参：实际参数，在调用函数中，传递参数
// 注意： 1、形参和实参要一一对应。
//       2、形参>实参 多余的形参为undefined
//       3、实参>形参 多余的实参  从 函数内的arguments对象中找

// 返回值：return
// return作用： 1、终止函数 
//              2、给函数“一个”返回值，以便在外部使用
//              3、return后不要跟任何代码

// 作用域：变量起作用的范围
// 分类： 全局作用域 局部作用域
// 变量分类：全局变量 局部变量
// ES5 函数作用域
// ES6 块级作用域 let
// var 和 let的区别： （1）let块级作用域  var是函数作用域
//                   （2）var支持变量提升（js解析过程 ： 预解析（var function）->解析 ）
//                   （3）let 存在暂时性死区
//                   （4） var可以重复声明相同变量名  let 只能申明一次

//  名词解释
// 闭包
// 高阶函数
// 递归（阶乘）
// 匿名函数

// 递归（深拷贝）
// 为什么需要深拷贝
// let arr = [1,2,3,4]
//let arr1 = arr  // 传址
//浅拷贝
// let arr1 = []
// for(let i=0;i<arr.length;i++){
//     arr1[i] = arr[i]
// }
// console.log(arr1)

// 深拷贝
// let arr = [[1,2],[3,4],[5,6]]
// let arr1 = []
// for(let i=0;i<arr.length;i++){
//     arr1[i] = arr[i]
// }

// function deepCopy(arr){
//     let newArr = []
//     for(let i=0;i<arr.length;i++){
//         if(typeof arr[i] != "object"){
//             newArr[i]=arr[i]
//         }else{
//             newArr[i] = deepCopy(arr[i])
//         }
//     }
//     return newArr
// }
// let arr = [1,2,3,[4,5]] 
// let arr2 = deepCopy(arr)
// arr[3][1] = "aa"
// console.log(arr)
// console.log(arr2)


// 斐波那契数列 
// 1 1 2 3 5 8 13 21 34
// 0 1 2 3 4 5 6  7  8

// 传参 数列的长度
// function fn(n){
//     let x=y=1
//     let arr = []
//     for(let i=0;i<n;i++){
//         if(i<=1){
//             arr.push(1)
//         }else{
//             arr.push(x+y)
//             let num = x+y
//             x = y
//             y = num 
//         }
//     }
//     return arr
// }
// console.log(fn(10))

