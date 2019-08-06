// 内置顶层函数
// console.log(escape("!"))   // 对非字母数字进行编码
// console.log(unescape("%21")) //对非字母数字进行解码

// console.log(Number("123")) //对数值型字符串进行转化 否则为NaN

// console.log(parseInt("1234.1234"))
// console.log(parseInt(1234.1234))
// console.log(parseInt('a123.123'))  //NaN
// console.log(parseInt('123.123a'))

// console.log(parseFloat("1234.1234"))
// console.log(parseFloat(1234.1234))
// console.log(parseFloat('a123.123'))  //NaN
// console.log(parseFloat('123.123a'))

// console.log(Boolean("a"))  //true
// console.log(Boolean("1"))  // true
// console.log(Boolean(""))  //false
// console.log(Boolean(+0))  //false
// console.log(Boolean(-0))
// console.log(Boolean(NaN))
// console.log(Boolean(null))
// console.log(Boolean(undefined))


// console.log(String(123))
// console.log(String(NaN))
// console.log(String(null))

// 对象：具体的人、事物
// 面向过程 面向对象 => 编程的模式
// 问题：把大象装冰箱需要几步？
// 面向过程：1、开冰箱 2、把大象装进去 3、关闭冰箱
// 面向对象：
// 大象：1、进冰箱
// 冰箱：1、开门 2、关门




// 五子棋
// 面向过程：
/*
1、绘制棋盘
2、白棋落子
3、黑棋落子
4、判断输赢
5、出结果

面向对象：
1、棋盘：绘制棋盘
2、棋子：落子
3、规则：判断输赢
*/

//创建对象
// 语法
/*
1、通过json方式创建
let ele = {方法名1:方法值1,方法2:方法值2}
*/
// let ele = {
//     'in':function(){
//         console.log("进入冰箱")
//     },
//     'out':function(){
//         console.log("出冰箱")
//     }
// }



// // 调用对象（属性方法）的语法
// // 对象名.方法名


// ele.in()
// ele.out()



// Person 人

// let person = {
//     eat:function(){
//         console.log("我在吃饭")
//     }, //方法
//     name:"小白",// 属性
//     sex:'男',
//     age:18,
//     say:function(){
//         console.log("我的姓名是"+this.name)
//     }
// }
// person.name = "小红"
// person.say()
// person.eat()


// Car类
// 属性 
/*
车型：轿车、SUV、SPV、
produce : 美国（别克、Jeep 、林肯、福特）德国（奔驰、大众）日本（丰田、日产、三菱、）中国（BYD、红旗）
color:

*/
// 方法
/*
run:
加油
*/





/*
1、创建对象的方式
（1）json
let obj = {键:值,键:值}
let person = {name:'horns',sex:'女',age:18}
（2）通过构造函数来创建
类：对象的抽象
对象：类的实例化
function Person(){
    this.name = ""
    this.sex = "男"
    this.age = 1
}

let p = new Person()

（3）通过类方式创建对象
class 类名{
    
}
(4) let obj = new Object()  // let obj = {}
obj.name = "xm"
obj.sex = "男"





2、调用对象的方式
person.name
person['name']




*/

// let person = {name:'horns',sex:'女',age:18}
// console.log(person.name)
// console.log(person['name'])
// let aa = "name"
// console.log(person[aa])


// function Person(){
//     this.name = ""   // this 谁实例化 指向谁 实例化对象
//     this.sex = "男"
//     this.age = 1
// }

// let p = new Person()
// let xm = new Person()
// console.log(p.name)
// console.log(p.sex)
// console.log(p.age)

// xm.name="小明"
// xm.sex = "女"
// console.log(xm.name)
// console.log(xm.sex)
// console.log(xm.age)


// class Fly{
//     constructor(){   //构造函数
//         this.name = ""
//         this.color = ""
//     }
// }

// let f1 = new Fly()
// let f2 = new Fly()
// f1.name = "C919"
// f1['color']="蓝&绿"
// console.log(f1.name,f1.color)
// f2.name = "波音"
// f2.color = "红色"
// console.log(f2.name,f2.color)



// let obj = new Object()  //{}
// obj.name = "小白"
// obj.sex = "男"
// obj.say = function(){
//     console.log(this.name)
// }
// console.dir(obj)


// class Person1{
//     constructor(){
//         this.name = "小白"
//     }
// }

// function Person2(){
//     this.name = "小白"
// }
// Person2.prototype = {
//     say:function(){},
//     run:function(){}
// }

// let p = new Person2()
// console.dir(p)
// console.dir(Person2)

// prototype（原型） 函数的方法, __porto__ 对象的方法
// 原型链 



// 总结
// 对象如何创建
/*
对象： 所要研究的 人、事物、规则、计划等都可以是对象
类： 对象的抽象

一、直接创建对象
   1、 json
   2、 new Object()
二、先创建 类 然后实例化对象
   1、通过构造函数
   3、通过 class关键字


*/

// 对象如何调用
/*
对象.属性名
对象['属性名']
*/


//原型以及原型链
// 原型：实现属性共享
/*
function Person(){
    属性
}
Person.prototype={
    方法名:function(){}
}


// prototype  __proto__  函数
// __proto__ 对象独有

原型链

function Person(){}
Person.prototype={
    say:function(){alert('我是人')}
}
let obj = new Person()



*/

// function Person(){}
// Person.prototype={
//     say:function(){alert('我是人')}
// }
// let obj = new Person()
// console.dir(obj)
// console.dir(Person)


// 一切皆对象

// let arr = [1,2,3]
// console.dir(arr)


let str = new String("123")
console.dir(str)
// let num = new Number(123)
// console.dir(num)


