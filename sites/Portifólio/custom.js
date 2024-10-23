console.log("Gabriel Walendolf");

let carro = new Object();
carro.marca = "Fiat";
carro.cor = "Azul";
carro.ano = "2000";
console.log(carro);

document.getElementById("carro").value = carro.marca;
document.getElementById("cor").value = carro.cor;
document.getElementById("ano").value = carro.ano;

carregarDados = () => {
    let carro = new Object();
    carro.marca = document.getElementById("carro").value;
    carro.cor = document.getElementById("cor").value;
    carro.ano = document.getElementById("ano").value;
    console.log("Carro: " + carro.marca + ", cor: " + carro.cor + ", ano: " + carro.ano);
}
