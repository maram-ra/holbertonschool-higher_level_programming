document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const characterDiv = document.getElementById('character');
        characterDiv.textContent = data.name;
      })
      .catch(error => console.error('Error fetching character:', error));
  }); 