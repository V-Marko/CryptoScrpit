function socket() {
    var socket = io();
    socket.on('connect', function () {
        console.log('Connected to server');
    });
    socket.on('btc_price', function (data) {
        console.log('Price:', data.price);
        data = Number(data.price).toString();
        document.getElementById('price').innerText = data;
    });
    socket.on('disconnect', function () {
        console.log('Disconnected from server');
    });
}







returnCrypto();
socket();