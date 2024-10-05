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
    const content = document.getElementById('content');

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
      if (isScrolling) {
        stopScrolling();
      } else {
        startScrolling();
      }
    });

    scrollResetButton.addEventListener('click', () => {
      scrollContainer.scrollTo(0, 0);
      stopScrolling();
      scrollSpeed = 1;
      // Restaure o estado original das cifras
      content.innerHTML = originalContent;
    });

    transposeUpButton.addEventListener('click', () => {
      transposeChords(1, 'sharp');
    });

    transposeDownButton.addEventListener('click', () => {
      transposeChords(-1, 'flat');
    });

    fontSizeUpButton.addEventListener('click', () => {
      adjustFontSize(1);
    });

    fontSizeDownButton.addEventListener('click', () => {
      adjustFontSize(-1);
    });

    function transposeChords(semitones, preference) {
      const chords = content.querySelectorAll('b,i');
      chords.forEach(chord => {
        chord.innerHTML = transposeChord(chord.innerHTML, semitones, preference);
      });
    }

    function transposeChord(chord, semitones, preference) {
      const sharpKeys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
      const flatKeys = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];
      
      const chordRegex = /^([A-G])(b|#)?(.*)$/;
      const match = chord.match(chordRegex);
      
      if (!match) return chord;

      let [_, root, accidental, suffix] = match;

      accidental = accidental || '';

      let index;
      if (preference === 'sharp') {
        index = (sharpKeys.indexOf(root + accidental) + semitones + 12) % 12;
        root = sharpKeys[index];
      } else if (preference === 'flat') {
        index = (flatKeys.indexOf(root + accidental) + semitones + 12) % 12;
        root = flatKeys[index];
      } else {
        index = (sharpKeys.indexOf(root + accidental) + semitones + 12) % 12;
        root = sharpKeys[index];
      }

      return root + suffix;
    }

    function adjustFontSize(amount) {
      const currentFontSize = parseFloat(window.getComputedStyle(content, null).getPropertyValue('font-size'));
      content.style.fontSize = (currentFontSize + amount) + 'px';
    }
  });