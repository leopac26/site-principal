document.addEventListener('DOMContentLoaded', () => {
    let isScrolling = false;
    let scrollSpeed = 1;
    let scrollInterval;
    const scrollContainer = document.getElementById('scroll-container');
    const scrollUpButton = document.getElementById('scroll-up');
    const scrollDownButton = document.getElementById('scroll-down');
    const scrollToggleButton = document.getElementById('scroll-toggle');
    const scrollResetButton = document.getElementById('scroll-reset');
    const transposeUpButton = document.getElementById('transpose-up');
    const transposeDownButton = document.getElementById('transpose-down');
    const fontSizeUpButton = document.getElementById('font-size-up');
    const fontSizeDownButton = document.getElementById('font-size-down');
    const mudarFundo = document.getElementById('muda-cor');
    const content = document.getElementById('content');
    const bodyFundo = document.body;

    // Armazene o estado original das cifras
    const originalContent = content.innerHTML;

    function startScrolling() {
        if (!isScrolling) {
            scrollInterval = setInterval(() => {
                scrollContainer.scrollBy(0, scrollSpeed);
            }, 200);
            isScrolling = true;
            scrollToggleButton.textContent = 'Pause';
        }
    }

    function stopScrolling() {
        if (isScrolling) {
            clearInterval(scrollInterval);
            isScrolling = false;
            scrollToggleButton.textContent = 'Play';
        }
    }

    scrollUpButton.addEventListener('click', () => {
        scrollSpeed = Math.max(scrollSpeed - 1, 1);
    });

    scrollDownButton.addEventListener('click', () => {
        scrollSpeed += 1;
    });

    scrollToggleButton.addEventListener('click', () => {
        isScrolling ? stopScrolling() : startScrolling();
    });

    scrollResetButton.addEventListener('click', () => {
        scrollContainer.scrollTo(0, 0);
        stopScrolling();
        scrollSpeed = 1;
        content.innerHTML = originalContent;
    });

    mudarFundo.addEventListener('click',function(){
        if(content.style.color === 'white'){
          content.style.color = 'black';
        }else{content.style.color = 'white'}

        if(bodyFundo.style.backgroundColor === 'black'){
          bodyFundo.style.backgroundColor = 'white';
        }else{bodyFundo.style.backgroundColor = 'black'}
      })

    transposeUpButton.addEventListener('click', () => {
        transposeChords(1); // Transpor para cima
    });

    transposeDownButton.addEventListener('click', () => {
        transposeChords(-1); // Transpor para baixo
    });

    fontSizeUpButton.addEventListener('click', () => {
        adjustFontSize(1); // Aumentar tamanho da fonte
    });

    fontSizeDownButton.addEventListener('click', () => {
        adjustFontSize(-1); // Diminuir tamanho da fonte
    });

    function transposeChords(semitones) {
        const chords = content.querySelectorAll('b');
        chords.forEach(chord => {
            chord.innerHTML = transposeChord(chord.innerHTML, semitones);
        });
    }

    function transposeChord(chord, semitones) {
        const sharpKeys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
        const flatKeys = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];

        const chordRegex = /^([A-G])(b|#)?(.*)$/; // Regex para capturar a raiz, acidentais e sufixos
        const match = chord.match(chordRegex);

        if (!match) return chord; // Retorna o acorde original se não corresponder ao regex

        let [_, root, accidental, suffix] = match;
        accidental = accidental || '';

        let isFlat = accidental === 'b';
        let keys = isFlat ? flatKeys : sharpKeys;

        let index = keys.indexOf(root + accidental);
        if (index === -1) return chord; // Retorna o acorde original se não encontrar o índice

        index = (index + semitones + 12) % 12;
        let newChord = keys[index];

        return newChord + suffix; // Retorna o acorde transposto com o sufixo
    }

    function adjustFontSize(amount) {
        const currentFontSize = parseFloat(window.getComputedStyle(content, null).getPropertyValue('font-size'));
        content.style.fontSize = (currentFontSize + amount) + 'px';
    }

    //let hideTimeout;

    // Função para mostrar os botões
   /* function mostrarBotoes() {
        scrollToggleButton.style.display = 'block';
        scrollUpButton.style.display = 'block';
        scrollDownButton.style.display = 'block';
        scrollResetButton.style.display = 'block';
        transposeUpButton.style.display = 'block';
        transposeDownButton.style.display = 'block';
        fontSizeUpButton.style.display = 'block';
        fontSizeDownButton.style.display = 'block';

        // Limpa o temporizador anterior
        clearTimeout(hideTimeout);

        // Oculta os botões após 8 segundos
        hideTimeout = setTimeout(esconderBotoes, 8000);
    }

    // Função para esconder os botões
    function esconderBotoes() {
        scrollToggleButton.style.display = 'none';
        scrollUpButton.style.display = 'none';
        scrollDownButton.style.display = 'none';
        scrollResetButton.style.display = 'none';
        transposeUpButton.style.display = 'none';
        transposeDownButton.style.display = 'none';
        fontSizeUpButton.style.display = 'none';
        fontSizeDownButton.style.display = 'none';
    }*/

    // Detectar toque na tela em dispositivos móveis
    // document.addEventListener('touchstart', mostrarBotoes);
    // document.addEventListener('click', mostrarBotoes);
});
