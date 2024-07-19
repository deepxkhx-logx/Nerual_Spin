// console.log("jay shree ram");
let uploader = document.querySelector('.uploader');
let fileInput = document.getElementById('file');
let imgSrc = document.querySelector('.uploader img');
let box = document.querySelector('.box');
let w_input = document.getElementById('width');
let h_input = document.getElementById('height');
let downloadBtn = document.querySelector('.downloadBtn');
let reduce_q = document.getElementById('reduce');
let aspect = document.getElementById('aspect');

let imgageRatio;

fileInput.addEventListener('change', (e) =>{
    let file = e.target.files[0];
    if(!file){
        return;
    }
    imgSrc.src = URL.createObjectURL(file);
    imgSrc.addEventListener('load', ()=>{
        box.classList.add('active');
        w_input.value = imgSrc.naturalWidth;
        h_input.value = imgSrc.naturalHeight;
        imgageRatio = imgSrc.naturalWidth/imgSrc.naturalHeight;
    })
})

uploader.addEventListener('click', ()=>{
    fileInput.click();
});

w_input.addEventListener('keyup', ()=>{
let height = aspect.checked ? w_input.value / imgageRatio : h_input.value;
h_input.value = Math.floor(height);
})
h_input.addEventListener('keyup', ()=>{
let width = aspect.checked ? h_input.value * imgageRatio : w_input.value;
w_input.value = Math.floor(width);
})

downloadBtn.addEventListener('click', ()=>{
    let canvas = document.createElement('canvas');
    let ctx = canvas.getContext('2d');

    canvas.width = w_input.value;
    canvas.height = h_input.value;

    let r_q = reduce_q.checked ? 0.5 : 1.0;

    ctx.drawImage(imgSrc, 0, 0, canvas.width, canvas.height);

    let a = document.createElement('a');
    a.download = new Date().getTime();
    a.href = canvas.toDataURL('image/jpeg', r_q);
    a.click();
})