// Assuming you have a JSON file containing scraped data
fetch('real_estate_data.json')
  .then(response => response.json())
  .then(data => {
    const propertyList = document.getElementById('property-list');

    data.forEach(property => {
      const propertyElement = document.createElement('li');
      propertyElement.classList.add('property');

      propertyElement.innerHTML = `
        <h2>${property.title}</h2>
        <p>${property.price}</p>
        <p>${property.address}</p>
      `;

      propertyList.appendChild(propertyElement);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });