let priceTable = [
    {code: '001', name: 'pilus', price: 10000},
    {code: '002', name: 'dedek gemesh', price: 20000},
    {code: '003', name: 'Cilok Goreng', price: 30000},
];

function getProduct(code) {
    return priceTable.find(product => product.code === code);
}

function calculateTotal(product, quantity) {
    return product.price * quantity;
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    let productCode = event.target.namakKode.value;
    let quantity = parseInt(event.target.banyakBarang.value);
    let cost = parseInt(prompt("Masukkan Jumlah Uang"));

    let product = getProduct(productCode);
    if (product) {
        let total = calculateTotal(product, quantity);
        alert("Total Harga: " + total);

        let returnOfCash = cost - total;
        alert("Kembalian: " + returnOfCash);
    } else {
        alert("Kode Barang Tidak Ditemukan");
    }
});