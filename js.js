const socket = io(); // подключение к Flask-SocketIO
const valueElement = document.querySelector('.Value');

socket.on('btc_price', data => {
    valueElement.textContent = `$ ${parseFloat(data.price).toFixed(2)}`;
});