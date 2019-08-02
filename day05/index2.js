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

let person = {
    eat:function(){
        console.log("我在吃饭")
    }, //方法
    name:"小白",// 属性
    sex:'男',
    age:18,
    say:function(){
        console.log("我的姓名是"+this.name)
    }
}
person.name = "小红"
person.say()
person.eat()


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



