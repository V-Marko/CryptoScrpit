var socket = io();
socket.on('connect', function () {
});
let CryptoOne = 0;
socket.on('btc_price', function (data) {
    data = Number(data.price).toString();
    document.getElementById('price').innerText = data;


    if (CryptoOne == 0) {
        ReturnCrypto();
    }

});
socket.on('disconnect', function () {
});


let ArrayCrypto = ["./BTC.png", "./DOGE.jpg", "./ETH.png", "./FTN.png", "./SOL.jpg"]
let ArrayText = ["BTC", "DOGE", "ETH", "FTN", "SOL"]

function ReturnCrypto() {
    CryptoOne += 1;
    const CryptoAllDiv = document.querySelector(".AllCrypto");
    for (let i = 0; i < ArrayCrypto.length; i++) {
        CryptoAllDiv.innerHTML +=
            `
                <div class="${ArrayText[i]} CryptoValue">
                    <img src="static/${ArrayCrypto[i]}" alt="${ArrayText[i]}">
                    <p>${ArrayText[i]}</p>
                    <p class="Value">$ <span id="price">-</span></p>
                </div>
        `
    }
}