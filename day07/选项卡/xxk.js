window.onload=function(){
    // 窗口加载事件

    let btns = document.querySelectorAll(".btns div")
    let cons = document.querySelectorAll(".cons div")
    let colors = ['pink','yellowgreen','orange']
    cons[0].style.zIndex = 10
    btns.forEach((item,index)=>{
        item.style.backgroundColor = colors[index]
        cons[index].style.backgroundColor = colors[index]

        item.onmouseenter = function(){
            cons.forEach(function(item,index){
                item.style.zIndex = 0
            })
            cons[index].style.zIndex = 10

        }
    })

    // 移入事件



}

