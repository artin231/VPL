const box1 = document.getElementById('box1')
const box2 = document.getElementById('box2')
const box3 = document.getElementById('box3')
const box4 = document.getElementById('box4')

box1.addEventListener('mouseenter', () => {
    box2.style.opacity = '0.5';
    box3.style.opacity = '0.5';
    box4.style.opacity = '0.5';
});
box1.addEventListener('mouseleave', () => {
    box2.style.opacity = '1';
    box3.style.opacity = '1';
    box4.style.opacity = '1';
});

box2.addEventListener('mouseenter', () => {
    box1.style.opacity = '0.5';
    box3.style.opacity = '0.5';
    box4.style.opacity = '0.5';
});
box2.addEventListener('mouseleave', () => {
    box1.style.opacity = '1';
    box3.style.opacity = '1';
    box4.style.opacity = '1';
});
box3.addEventListener('mouseenter', () => {
    box1.style.opacity = '0.5';
    box2.style.opacity = '0.5';
    box4.style.opacity = '0.5';
});
box3.addEventListener('mouseleave', () => {
    box1.style.opacity = '1';
    box2.style.opacity = '1';
    box4.style.opacity = '1';
});

box4.addEventListener('mouseenter', () => {
    box1.style.opacity = '0.5';
    box3.style.opacity = '0.5';
    box2.style.opacity = '0.5';
})
box4.addEventListener('mouseleave', () => {
    box1.style.opacity = '1';
    box3.style.opacity = '1';
    box2.style.opacity = '1';
});