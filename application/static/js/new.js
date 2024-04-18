function Images() {
    let image= document.getElementById('img')

    if(image.src.match("bluzhugo.webp")) {
image.src = "hugo2.jpeg"

    } else {
        image.src= "bluzhugo.webp"
    }
}
function test() { 
let image= document.getElementById('versace')
    if(image.src.match("bluzversace.webp")) 
    { image.src ="versace.png"
}
    else{
        image.src= "bluzversace.webp"
    }
     }
