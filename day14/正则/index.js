let arr1 = ['99912341234',"15723553456",'a1251566234','136121348590',"13635353667","17634666535"]

let str2 = "<span>this is span</span>"

// 正则
// 正则对象: 将一个规则形成一个对象方便使用。
// 正则表达式: 用来描述或者匹配一系列符合某种规则的字符串的表达式。
//创建正则对象语法

// let re = new RegExp('正则表达式','模式')
// 模式  g 全局匹配   i 忽略大小写  m 多行匹配

// let re = /正则表达式/模式
// 正则表达式常用的方法
// re.exec() 返回 匹配符合正则表达式规则的字符串信息 ，如果没有匹配到 返回 null

// re.test() 所匹配的字符串是否符合正则表达式规则 返回值true false

// let re = /abc/
// let str1 = "abcdefgabc"
// console.log(re.test(str1))

// let re = /^abc$/gim
// let str1 = `
// abc
// ABC
// abc
// `
// console.log(re.exec(str1))
// console.log(re.exec(str1))
// console.log(re.exec(str1))

//正则表达式
// 元字符
/*
\d  数字
\D  非数字
\w  字母数字下划线
\W  非字母数字下划线
\s  空
\S  非空
\b  单词边界
.   所有字符
*/
// let re = /i\b/
// let arr = ['a','b','c','1'," ",'2','3',9,10,"_","%b%"]
// let str = "thisi is box"
// for(let i=0;i<arr.length;i++){
//     console.log(re.exec(arr[i]))
// }
// console.log(re.exec(str))

// 原子表
// [][^]
// let re = /[^\d,\s]/
// let arr = ['a','b','c','1'," ",'2','3',9,8,"_","%b%"]
// for(let i=0;i<arr.length;i++){
//     console.log(re.exec(arr[i]))
// }

// 数量 {1}1位 {10} 10位 {10,} 至少10位 {10,15} 10~15 
// + 一个或多个   * 0个或多个  ? 1个或0个

// 特殊用法
// ()分组    |或   . 任意内容

// re = /^(136|157|176)\d{8}$/
// arr1.forEach((item)=>{
//     console.log(re.exec(item))
// })

//匹配邮箱
// let arr = [
//     '842615663@qq.com',
//     'wetjih@163.com',
//     'we234tjih@163.cn',
//     'we234tjih@qq.cn',
//     'wqeotq345@yahoo.com.cn',
//     '842615663@qq',
//     '842615663qq.com',
//     '@qq.com'
// ]
// let re = /^\w+@(qq|163|yahoo)\.(com|cn)(\.cn)?$/
// arr.forEach((item)=>{
//     console.log(re.exec(item))
// })


// let str = 'http://soso.huitu.com/search/sdfaag.html?kw=中元节'
// let str3 = "https://www.baidu.com/sdfa/asdf/?name=horns&age=18"

// let re = /(http:\/\/|https:\/\/)([\w,.]+)\/([\w,\/,\.]*)\?([\w,=,\u4e00-\u9fa5,&]*)/
// console.log(re.exec(str3))


// 特点 ：正则表达式在匹配时 都是 采用贪婪模式
// ?
// let str = "a12345a67890a"
// let re = /a\w+?a/
// console.log(re.exec(str))

let str1 = `<div class="box">
<div class="son">this is div</div>
</div>`

let re = /<[\w,\s,=,",']+>\n<[\w,\s,=,",']+>([\w,\s]+)<[\w,\s,=,",',\/]+>\n<[\w,\s,=,",',\/]+>/
console.log(re.exec(str1))
let str3 = `<div class="box">
    <div class="son1">this is box</div>
    <div class="son2">this is box</div>
    <div class="son3">this is box</div>
    <div class="son4">this is box</div>
    <div class="son5">this is box</div>
</div>`