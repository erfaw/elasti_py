const container= document.querySelector('.container');
const panels= document.querySelectorAll('.panel');
container.setAttribute('style','width:60vw; transition: width 1s ease;');
// let i=0;
// for(let panel of panels){
//     panel.addEventListener('click',()=>{
//         if(panel.classList.contains('active')) panel.classList.remove('active');
//         else{
//             removeActiveS();
//             addActive(panel);
//         }
//     })
// }
panels.forEach(panel => {
    panel.addEventListener('click',()=>{
        if(panel.classList.contains('active')) {
            panel.classList.remove('active');
        container. setAttribute('style','width:60vw; transition: width 1s ease;');
        }else{
            removeActiveS();
            addActive(panel);
            container. setAttribute('style','transition: 1s ease');

        }
    }) 
})

// panels.forEach(panel => {
//     if(panel.classList.contains('active')){
//         i+=1;
//     };
// });
// console.log(i);
// if (i==0){
//     container. setAttribute('style','width:60vw;');
// }else{
//     container. setAttribute('style','');
// }


function removeActiveS(){
    for(let panel of panels){
        panel.classList.remove('active');
    }
}
function addActive(p){
    p.classList.add('active');
}

