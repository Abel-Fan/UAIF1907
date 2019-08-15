$(function(){
    let btn = $(".btns div")
    let box = $(".boxs div")
    btn.eq(0).css({
        "background-color":"red",
    })
    box.eq(0).css({
        "z-index":10
    })
    btn.mouseenter(function(){
        let index = $(this).index()
        btn.css({
            "background-color":"",
        }).eq(index).css({
            "background-color":"red",
        })
        box.css({
            "z-index":0
        }).eq(index).css({
            "z-index":10
        })
    })




})