/*
一、函数：
二、语法：
1、定义：
    function 函数名([形参]){
        函数体
        [return 返回值]
    }
2、调用
    函数名([实参])


名词解释：
形参
实参
返回值：1、给函数一个返回值以便在函数外部使用。2、终止函数
*/

// 练习1： insert
// arr = [1,2,3,4,5]  0   3

// 先取index之前的
// newArr = [1,2,3]
// 把index插入
// newArr[index]=3
// 把index之后的元素插入
// 

// function insert(arr,item,index){
//     let newArr = []
//     for(let i=0;i<index;i++){
//         newArr[i] = arr[i]
//     }
//     newArr[index]=item
//     for(let j=index;j<arr.length;j++){
//         index+=1
//         newArr[index]=arr[j]
//     }
//     return newArr
// }
// let arr = [1,2,3,4,5]
// arr = insert(arr,'aa',5)


// 首部删除
// let arr = [1,2,3,4,5,6,7,8,9]

// function shift(arr){
//     let newArr = []
//     for(let i=1;i<arr.length;i++){
//         newArr[i-1] = arr[i]
//     }
//     return newArr
// }

// arr = shift(arr)
// console.log(arr)


// 末尾删除

