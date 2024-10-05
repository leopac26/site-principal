document.getElementById('searchButton').addEventListener('click', function() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const resultsDiv = document.getElementById('results');
    const links = document.querySelectorAll('#principal li');
  
    // Limpar resultados anteriores
    resultsDiv.innerHTML = '';
  
    // Filtrar links com base na entrada do usuário
    links.forEach(link => {
      const text = link.textContent.toLowerCase();
      if (text.includes(input)) {
        resultsDiv.innerHTML += `<p>${link.innerHTML}</p>`;
      }
    });
  
    // Mensagem se nenhum resultado for encontrado
    if (resultsDiv.innerHTML === '') {
      resultsDiv.innerHTML = '<p>Nenhum resultado encontrado.</p>';
    }
  });