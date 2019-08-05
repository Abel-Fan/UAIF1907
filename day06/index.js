// let str = new String("abc")
// console.dir(str)

// let str1 = "abcdef"
// console.log(str1.charAt(0))
// console.log(str1.charCodeAt(0))

// console.log(String.fromCharCode(97))

// let str = "abc"
// console.log(str.indexOf('ab'))
// console.log(str.indexOf('d'))

// let str = "abcdef"
// console.log(str.search("g"))
// console.log(str.search('de'))

// let str = "abcdef"
// console.log(str.match("g"))
// console.log(str.match('d'))

// let str = "abcdefa"
// console.log(str.lastIndexOf("a"))
// console.log(str.lastIndexOf("z"))

// let str = "山西优逸客"
// console.log(str.replace('山西','陕西'))


// let str = "abcdefgh"
// console.log(str.substring(0,5))  // abcdef
// console.log(str.substring(0))   // abcdefgh

// let str = "abcdefgh"
// console.log(str.substr(1,5))  // bcdef

// let str = "abcdefgh"
// console.log(str.slice(0,5))  // abcde 从 0位开始到 end之前
// console.log(str.slice(0))   // abcdefgh

// let str = "a b c d e f"
// console.log(str.split(" ")) //['a','b'....]
// console.log(str.split())  // ['a b c ...']


// let str = "AsdfdfdDD"
// console.log(str.toLowerCase())  // asdfdfddd
// console.log(str.toUpperCase())  // ASDFDFDDD

// let str = new String("    a  b  c   ")
// console.dir(str)
// // console.log(str.repeat(10))
// // console.log(str.startsWith("b"))
// console.log(str.trim())

// a-z

// String.fromCharCode()

// console.log( String.fromCharCode( parseInt(Math.random()*26)+65  )  )


let array = [1,2,3,4,5,6]

// let arr = [1,2,3,4,5,6,7,8,9]
// console.log(arr.unshift('a','b','c'))  // 12
// console.log(arr)   //['a','b','c',1,2,3,4,5,6,7,8,9]

// let arr = [1,2,3]
// console.log(arr.shift())  // 1
// console.log(arr)  // [2,3]

// let arr = [1,2,3]
// console.log(arr.push("a",'b','c'))  // 6
// console.log(arr) // [1,2,3,'a','b','c']

// let arr = [1,2,3]
// console.log(arr.pop())  // 3
// console.log(arr)  // [1,2]

// let arr = [1,2,3,4,5,6,7,8,9]
// console.log(arr.splice(5))  // [6,7,8,9]  删除数组中从start开始到结尾的所有元素，返回被删除的元素
// console.log(arr) // [1,2,3,4,5]

// let arr = [1,2,3,4,5,6,7,8,9]
// console.log(arr.splice(3,5,'a','b','c')) // [4,5,6,7,8] 删除数组中从start开始5个元素，并且在start位置插入 'a','b','c' 。返回值是被删除的元素
// console.log(arr) //[1,2,3,'a','b','c',9]

// let arr = [1,2,3,4,5]
// console.log(arr.join(","))
// console.log(arr)  // "1,2,3,4,5"

// let arr = [1,2,3]
// console.log(arr.concat(['a','b','c'])) // [1,2,3,'a','b','c']
// console.log(arr) // [1,2,3]

// let arr = [1,2,3,4,5,6,7,8,9]
// console.log(arr.slice(2,5))  // [3,4,5]
// console.log(arr.slice(4))   // [5,6,7,8,9]
// console.log(arr)  // [1,2,3,4,5,6,7,8,9]

// let arr = [1,2,3,4,3,6,7,4]
// console.log(arr.sort())
// arr.sort(function(a,b){return b-a})
// console.log(arr)


// 从arr中找到第一个大于5的元素
// let arr = [1,2,3,4,5,878,7,8,9] 
// console.log(arr.find( a=>{if(a>5)return a}  ))

// let arr = [1,2,3,4,5,6,7,8,9]
// console.log(arr.findIndex( a=>{if(a>5)return a} )) //5

// let arr = [1,2,3,4,5,6,7,8,9]
// console.log(  arr.filter((a)=>{ if(a%2==0)return a }))\

// let arr = [1,2,3,4,5,6,7,8]
// console.log( arr.some(a=>{ if(a>9)return a}) ) 
// //false 测试是否有元素大于9
// console.log( arr.some(a=>{if(a%2==0)return a}))
// //true 测试是否有元素是偶数

// let arr = [1,2,3,4,5]
// console.log( arr.every(a=>{ if(a<10)return a }))
// // 是否每一个都小于10
// console.log( arr.every(a=>{ if(a%2==0)return a}))
// // 是否每一个都为偶数

// let arr = [1,2,3,4,5,6]
// console.log(arr.includes('1'))

// let arr = [1,2,3,4,5,6]
// console.log(arr.forEach((item,index)=>{console.log(item,index)}))
// // console.log(arr)


// let arr = [1,2,3,4,5,6]
// console.log(arr.map(  item=>item*item  ))

let arr = [1,2,3,4,5,6]
console.log(arr.reverse())  //[6,5,4,3,2,1]