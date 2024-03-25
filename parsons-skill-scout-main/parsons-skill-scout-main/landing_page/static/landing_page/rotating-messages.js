const rotatingText = document.getElementById('rotating-text');
const messages = [
  'Discover your dream job',
  'Find the perfect match for your skills',
  'Unlock new career opportunities'
];


let currentIndex = 0;


function rotateMessages() {
  rotatingText.style.opacity = 0;
  setTimeout(() => {
    rotatingText.textContent = messages[currentIndex];
    currentIndex = (currentIndex + 1) % messages.length;
    rotatingText.style.opacity = 1;
  }, 0);
}


rotateMessages();


setTimeout(() => {
  setInterval(rotateMessages, 3000);
}, 0);