

/*const songContainer = document.getElementById('resultado');
const playPauseButton = document.getElementById('playPauseButton');
const increaseSpeedButton = document.getElementById('increaseSpeed');
const decreaseSpeedButton = document.getElementById('decreaseSpeed');
let isPlaying = false;
let scrollInterval;
let scrollSpeed = 1; // pixels por passo
let lastScrollTop = 0;
let lastScrollTime = Date.now();

playPauseButton.addEventListener('click', () => {
    if (!isPlaying) {
        playPauseButton.textContent = 'Pause';
        isPlaying = true;
        startScrolling();
    } else {
        playPauseButton.textContent = 'Play';
        isPlaying = false;
        clearInterval(scrollInterval);
    }
});

increaseSpeedButton.addEventListener('click', () => {
    scrollSpeed += 1;
});

decreaseSpeedButton.addEventListener('click', () => {
    if (scrollSpeed > 1) {
        scrollSpeed -= 1;
    }
});

function startScrolling() {
    scrollInterval = setInterval(() => {
        const currentTime = Date.now();
        const timeDiff = currentTime - lastScrollTime;
        const distance = scrollSpeed * (timeDiff / 100); // Ajuste para uma rolagem suave

        songContainer.scrollTop += distance;
        lastScrollTop = songContainer.scrollTop;
        lastScrollTime = currentTime;
    }, 100); // Aproximadamente 60fps
}*/

var tempo;
function rolar(e){
   if(e){
      var el = document.querySelector("#resultado");
      tempo = setInterval(function(){
         var doc_scrl = document.documentElement.scrollTop;
         
         if(el.offsetTop-doc_scrl <= window.innerHeight-el.offsetHeight){ // aqui é quando a janela chega ao fim
            clearInterval(tempo);
         }else{
            window.scroll(0,doc_scrl+2);
         }
      }, 500);

   }else{
      clearInterval(tempo);
   }
}


       document.addEventListener("DOMContentLoaded", function() {
            const scrollContainer = document.getElementById("scroll-container");
            const scrollText = document.getElementById("scroll-text");
            const toggleButton = document.getElementById("toggle-scroll");
            const speedControl = document.getElementById("speed-control");

            let scrollAmount = 0;
            let scrolling = false;
            let interval;
            let speed = speedControl.value;

            function scrollTextVertically() {
                scrollAmount -= 1;
                if (Math.abs(scrollAmount) >= scrollText.clientHeight) {
                    scrollAmount = scrollContainer.clientHeight;
                }
                scrollText.style.transform = `translateY(${scrollAmount}px)`;
            }

            function startScrolling() {
                if (!scrolling) {
                    interval = setInterval(scrollTextVertically, 100 / speed);
                    toggleButton.textContent = "Parar Rolagem";
                    scrolling = true;
                } else {
                    clearInterval(interval);
                    toggleButton.textContent = "Iniciar Rolagem";
                    scrolling = false;
                }
            }

            toggleButton.addEventListener("click", startScrolling);

            speedControl.addEventListener("input", function() {
                speed = speedControl.value;
                if (scrolling) {
                    clearInterval(interval);
                    interval = setInterval(scrollTextVertically, 100 / speed);
                }
            });
        });
   