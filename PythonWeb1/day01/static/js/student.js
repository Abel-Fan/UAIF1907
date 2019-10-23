function del(id){
    alert(id)
    // 删除 id 所对应的学生信息
    // 请求后台资源
    // 请求资源方式 ： 1、表单  2、a连接浏览器  3、ajax  XMLHTTPRequest
}
$(function(){
    // 编辑学生信息
    let edit = $(".edit")
    edit.click(function(){
        let tr = $(this).parents("tr")
        let children = tr.children("td")
        $(".editBox").show()
        let id = children.eq(0).text()
        $(".btn").attr("sid",id)
        $("[name=num]").val(children.eq(1).text())
        $("[name=name]").val(children.eq(2).text())
        console.log(children.eq(3).attr('val'))
        if( children.eq(3).attr('val')=='1' ){
            console.log(123)
            $('[name=sex]').eq(0).attr("checked","checked")
        }else{
            $('[name=sex]').eq(1).attr("checked","checked")
        }

        $("[name=age]").val(children.eq(4).text())
        $("[name=class]").val(children.eq(5).text())
    })

    $(".btn").click(function(){
        $.ajax({
            url:"edit",
            type:"post",
            data:{
                'id':$(".btn").attr("sid"),
                'num':$("[name='num']").val(),
                'name':$('[name=name]').val(),
                'age':$('[name=age]').val(),
                'sex':$('[name=sex]').val(),
                'class':$('[name=class]').val()
            },
            success:function(data){
                console.log(data)
            },
            error:function(e){
                console.log(e)
            }
        })
    })
})


 // $.ajax({
        //     url:"edit",
        //     type:"post",
        //     data:{
        //         'id':1,
        //         'num':'20190101',
        //         'name':'小白',
        //         'age':'20',
        //         'sex':1,
        //         'class':'UAIF1907'
        //     },
        //     success:function(data){
        //         console.log(data)
        //     },
        //     error:function(e){
        //         console.log(e)
        //     }
        // })