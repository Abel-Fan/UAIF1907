// window

// let mywin = window.open("http://www.baidu.com","优逸客",'width=200,height=200',false)
// mywin.moveBy()  // 移动窗口
// mywin.moveTo()  // 移动到指定位置
// mywin.resizeBy() // 修改尺寸
// mywin.resizeTo() // 修改尺寸到

// mywin.alert(123)

// setInterval(fn,1000)
// let index = 0
// let t = setInterval(function(){
//     console.log(index++)
//     if(index==10){
//         clearInterval(t)
//     }
// },1000)

// let t = setTimeout(function(){
//     console.log(123)
// },3000)

// clearTimeout(t)

// 面向对象的方式开发钟表 clock
// 电子表  钟表
// 属性：hour minute seconds
// 方法：run




// function Clock(h,m,s){
//     this.h = h
//     this.m = m
//     this.s = s
// }
// Clock.prototype.run = function(){

//     //方法1： 你可以用that来保存 Clock实例 
// //    // this // Clock实例
// //     let that = this
// //     setInterval(function(){
// //         // this  // window
// //         that.s
// //     },1000)

//     setInterval(()=>{
//         this.s+=1
//         if(this.s>=60){
//             this.s=0
//             this.m+=1
//             if(this.m>=60){
//                 this.m=0
//                 this.h+=1
//                 if(this.h>=24){
//                     this.h=0
//                 }
//             }
//         }
//         console.log(`${this.h}:${this.m}:${this.s}`)
//     },1000)


// }


// let c = new Clock(10,22,30)
// c.run()

//history

// console.dir(history)
//  length 历史记录的数量
//

//location 地址栏
console.dir(location)
console.log(location.href) //当前的URL
console.log(location.protocol) // 协议


