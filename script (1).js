// JSON ma'lumotlarni yuklash
fetch('dars_jadvali.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('jadval');
    data.forEach(dars => {
      const darsDiv = document.createElement('div');
      darsDiv.className = 'dars-item';
      darsDiv.innerHTML = `
        <h3>${dars.fan}</h3>
        <p>🕒 ${dars.vaqt} | 👨🏫 ${dars.oqituvchi}</p>
        <p>📅 ${dars.kun} (${dars.sana})</p>
      `;
      container.appendChild(darsDiv);
    });
  });

// Tema o'zgartirish
function changeTheme(theme) {
  document.body.className = theme;
}