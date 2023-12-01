setTimeout(() => {
    document.querySelectorAll(".card").forEach((e)=>{
        e.childNodes[1].style.opacity = 0
    })
}, 2000);
let images = [
    '../../../static/img/games/memory/foto1.jpeg',
    '../../../static/img/games/memory/foto1.jpeg',
    '../../../static/img/games/memory/foto2.jpeg',
    '../../../static/img/games/memory/foto2.jpeg',
    '../../../static/img/games/memory/foto3.jpeg',
    '../../../static/img/games/memory/foto3.jpeg',
    '../../../static/img/games/memory/foto4.jpeg',
    '../../../static/img/games/memory/foto4.jpeg'
]
images = images.sort(function(){return Math.random()-0.5})


for(let i = 0;i<images.length;i++){
    document.querySelector(".game").insertAdjacentHTML('beforeend', `<button class="card">
        <img src='${images[i]}' class="value">
    </button>`)
}

let results = []
let pairs = []
document.querySelectorAll(".card").forEach((e)=>{
    e.addEventListener("click", ()=> {
        e.childNodes[1].style.opacity = 1
        if(results.length==0){
            results.push(e)
        } else {
            if(results[0].childNodes[1].getAttribute("src") != e.childNodes[1].getAttribute("src")){
                document.querySelectorAll(".card").forEach((e)=>{
                    e.disabled = true
                })
                setTimeout(() => {
                    e.childNodes[1].style.opacity = 0
                    results[0].childNodes[1].style.opacity = 0
                    results.pop()
                }, 1000);
                
                setTimeout(() => {
                    document.querySelectorAll(".card").forEach((e)=>{
                        e.disabled = false
                        for(el of pairs){
                            el.disabled=true
                        }
                    })
                }, 1000);
                
            } else {
                pairs.push(e)
                pairs.push(results[0])
                results.pop()
                for(el of pairs){
                    el.disabled=true
                }
            }
        }
        
        if(pairs.length == images.length){
            function reset_game(){
                location.reload()
            }
            document.querySelector(".main").insertAdjacentHTML('beforeend', `
                <button class="button_reset">Jugar de nuevo</button>
            `)
            document.querySelector(".button_reset").onclick = reset_game
            
        }
        
    })
})