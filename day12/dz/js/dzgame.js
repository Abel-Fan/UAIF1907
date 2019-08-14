// 面向对象的方式
window.onload = function(){
    class Game{
        constructor(screenSel,btnSel,key){  //构造函数
            this.screen = document.querySelector(screenSel)
            this.btn = document.querySelector(btnSel)
            this.key = document.querySelector(key)
            this.letters = []
            this.isKill = false
            this.createLetter()
            this.runToggle()
            this.killLetter()
        }
        // 创建字母 num默认字母数量
        createLetter(num=5){
            for(let i=0;i<num;i++){
                let div = document.createElement("div")

                div.className = "letter"

                let letter = String.fromCharCode(Math.floor(Math.random()*26)+65)
                while(this.isRepeat(letter)){
                    // letter与this.letters里任何一个title都不一样
                    letter = String.fromCharCode(Math.floor(Math.random()*26)+65)

                }

                div.style.backgroundImage = `url(./img/A-Z/${letter}.png)`

                let left = Math.random()*(7.5-0.53)
                //解决重叠
                while(this.isOverlap(left)){   
                    //条件： left与之前所有字母的left的绝对值都不小于0.53
                    // isOverlap() 都不小于0.53 返回false  有小于0.53 返回 true
                    left = Math.random()*(7.5-0.53)
                }
                div.style.left = left+"rem"


                let top = Math.random()*1+1
                div.style.top = top+"rem"

                let obj = {'title':"",'left':"",'top':"",'node':''}
                obj.title = letter
                obj.left = left
                obj.top = top
                obj.node = div
                this.letters.push(obj)
                this.screen.appendChild(div)
            }
        }
        isOverlap(left){
            let index = this.letters.findIndex((item)=>{
                if(Math.abs(item.left-left)<0.53){
                    return item
                }
            })
            if(index!=-1){
                return true
            }else{
                return false
            }
        }
        isRepeat(letter){
            let index = this.letters.findIndex((item)=>{
                if(item.title==letter){
                    return item
                }
            })
            if(index!=-1){
                return true
            }else{
                return false
            }
        }
        run(){
            this.t = setInterval(()=>{
                this.letters.forEach((item,index)=>{
                    item.top+=0.3
                    item.node.style.top = item.top+"rem"
                    if(item.top>8.9){
                        this.removeChild(index)
                    }
                })
            },500)
        }
        // 控制暂停开始
        runToggle(){
            let flag = true
            this.btn.ontouchstart = ()=>{
                if(flag){
                    flag=false
                    this.run()
                    this.isKill = true
                }else{
                    flag = true
                    clearInterval(this.t)
                    this.isKill = false
                }
                
            }
        }
        // 消除字母
        killLetter(){
            this.key.ontouchstart = (event)=>{
                if(!this.isKill){
                    return 
                }
                let target = event.target
                if(target.nodeName=="SPAN"){
                    let lettter = target.innerText
                    let index = this.letters.findIndex((item)=>{
                        if(item.title==lettter){
                            return item
                        }
                    })
                    this.removeChild(index)
                }
            }
        }
        removeChild(index){
            this.screen.removeChild(this.letters[index].node)
            this.letters.splice(index,1)
            this.createLetter(1)
        }


    }

    let game = new Game(".screen",".zt",".key")
    



}

// 打字游戏
// 属性: 创建字母  运行 暂停  开始  消除字母
//http://soso.huitu.com/search?kw=%E4%B8%AD%E7%A7%8B
