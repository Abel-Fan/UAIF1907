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
// let arr = [1,2,3]
// function aa(arr){
//     console.log(arr)
//     arr=[33,44,55]
// }
// aa(arr)
// console.log(arr)


// 数组排序
// paixu(arr)
// 冒泡排序   选择排序
// 冒泡排序：两两交换
// [6,5,4,3,2,1]
// 1、  [5,6,4,3,2,1]
// 2、  [5,4,6,3,2,1]
// 3、  [5,4,3,6,2,1]
// 4、  [5,4,3,2,6,1]
// 5、  [5,4,3,2,1,6] 

// 1、[5,4,3,2,1,6]   5
// 2、[4,3,2,1,5,6]   4
// 3、[3,2,1,4,5,6]   3
// 4、[2,1,3,4,5,6]   2
// 5、[1,2,3,4,5,6]   1

// function fn(arr){
//     for(let i=0;i<arr.length-1;i++){
//         for(let j=0;j<arr.length-i-1;j++){
//             if(arr[j+1]>arr[j]){
//                 let num= arr[j+1]
//                 arr[j+1]=arr[j]
//                 arr[j]=num
//             }
//         }
//     }
//     return arr
// }
// console.log(fn([3,3,4,5,6,8,6,4,3,2,8,7,5]))


// 选择排序
// let arr = [1,2,3,4,5,6]

// 1 [6,2,3,4,5,1]
// 2 [6,5,3,4,2,1]
// 3 [6,5,4,3,2,1]
// 4 [6,5,4,3,2,1]
// 5 [6,5,4,3,2,1]

function fn2(arr){
    for(let i=0;i<arr.length-1;i++){
        let maxIndex = i
        for(let j=i+1;j<arr.length;j++){ 
           if(arr[j]>arr[maxIndex]){
               maxIndex=j
           }
        }
        if(maxIndex!=i){
            let num = arr[i]
            arr[i] = arr[maxIndex]
            arr[maxIndex] = num    
        }
    }
    return arr
}

console.log(fn2([1,2,3,2,1,3,5,6,4,3,2,5,9,7,8]))

