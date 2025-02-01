// JSON ma'lumotlarni yuklash
fetch('dars_jadvali.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('jadval');
        data.forEach(dars => {
            container.innerHTML += `
                <div class="dars-item">
                    <h3>📚 ${dars.C}</h3>
                    <p>🕒 Vaqt: ${dars.G}</p>
                    <p>👨🏫 O'qituvchi: ${dars.F}</p>
                    <p>📅 Kun: ${dars.A} (${dars.B})</p>
                    <p>📍 Joy: ${dars.D}</p>
                    <p>📝 Turi: ${dars.E}</p>
                </div>
            `;
        });
    })
    .catch(error => console.error("Xato:", error));

// Tema o'zgartirish funksiyasi
function changeTheme(theme) {
    document.body.className = theme;
}