window.onload=function(){
    // 窗口加载事件

    let btns = document.querySelectorAll(".btns div")
    let cons = document.querySelectorAll(".cons div")
    let colors = ['pink','yellowgreen','orange']

    btns.forEach((item,index)=>{
        item.style.backgroundColor = colors[index]
        cons[index].style.backgroundColor = colors[index]
    })


}

