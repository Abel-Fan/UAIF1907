// 初始数据类型：number string boolean undefined null
// 引用数据类型：数组
// 数组的定义：用来存储一系列相关数据的集合
// 语法：
// （1）let arr = [1,2,3,'a','b',true,undefined,null]
    // let arr = [1,2,3,'a','b',true,undefined,null]
    // console.log(arr)
//  (2) let arr = new Array(1,2,3,4,5)
    // let arr = new Array(1,2,3,4,5)
    // console.log(arr)
    // 注意：当只传入一个数值代表数组的长度，而非元素。
    // let arr = new Array(9)
    // console.log(arr)

let category = ['书籍','衣服','电子产品']
              // 0   1   2
//获取元素，访问元素
//语法
//  category[下标] 举例 category[1]
// console.log(category[1])
// 遍历，依次访问
// for(let i=0;i<3;i++){
//     console.log(category[i])
// }


// 长度  arr.length
// console.log(category.length)
// 增 删 改 查 

// 删
// delete category[1]
// console.log(category)
// console.log(category.length)
// category.length=0  // 全部删除
// console.log(category)
// console.log(category.length)


// 改
// category[1]="生活用品"
// console.log(category)

// 增加
// category[3]="衣服"
// console.log(category)
// category.push('家居') // 末尾添加
// console.log(category)

// 初始数据类型与应用数据类型的区别
// 1、初始数据类型存放在栈区
// 2、引用数据类型存放在堆区
//1、栈区（stack）— 由编译器自动分配释放 ，存放函数的参数名，局部变量的名等。其操作方式类似于数据结构中的栈。
//2、堆区（heap）— 由程序员分配释放， 若程序员不释放，程序结束时可能由OS回收。注意它与数据结构中的堆是两回事，分配方式倒是类似于链表。

// let num = 123
// let arr = [1,2,3]
// let num2 = num
// let arr2 = arr  // 对于引用数据 不能直接赋值（因为本质：赋址）应该拷贝
// console.log(num2)  //123
// console.log(arr2)  //[1,2,3]
// num2 = 321
// arr2[1]=4
// console.log(num2) // 321
// console.log(arr2) // [1,4,3]
// console.log(num) // 123
// console.log(arr) // [1,2,3]

let arr = [1,2,3]
let arr3 = []

// 拷贝 浅拷贝~
for(let i=0;i<arr.length;i++){
    arr3[i]=arr[i]
}
console.log(arr3)
arr3[2]="a"
console.log(arr3)
console.log(arr)