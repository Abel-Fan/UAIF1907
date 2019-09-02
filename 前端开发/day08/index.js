// 选项卡
function SelectCard(btnsClassName,consClassName){
    let btns = document.querySelectorAll(btnsClassName)
    let cons = document.querySelectorAll(consClassName)
    btns.forEach(function(item,index){
        item.onmouseenter = function(){
            // 清空所有按钮的类名
            btns.forEach(function(it,i){
                it.classList.remove("btnAction")
            })
            //设置当前的元素
            this.classList.add("btnAction")
            // 清空所有con的类名
            cons.forEach(function(it,i){
                it.classList.remove("conAction")
            })
            cons[index].classList.add("conAction")
        }
    })
}





