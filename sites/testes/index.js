let cookie = 0;
let cliques = 1; // Acumulativo: aumenta a cada compra
let incremento = 0; // Acumulativo: aumenta a cada compra
let intervaloAtivo = false; // Controla se o incremento está ativo
const contadorElemento = document.getElementById("cookie");

// Função para somar 1 ao contador ao clicar
function contar() {
  cookie += cliques; 
  contadorElemento.innerText = cookie.toFixed(1);
}

// Função para "comprar" (diminuir 10 cookie e aumentar o incremento em 0.2)
function comprar_empreendedor() {
  if (cookie >= 10) {
    // Verifica se há cookie suficientes
    cookie -= 10;
    incremento += 0.1; // Aumenta o incremento em 0.2 a cada compra
    contadorElemento.textContent = cookie.toFixed(1);

    if (!intervaloAtivo) {
      // Ativa o incremento automático uma vez
      empreendedor();
    }
  } else {
    alert("Cookies insuficientes!");
  }
}
// Função para comprar clique (diminuir 10 cookie e aumentar o clique em 0.2)
function comprar_clique() {
  if (cookie >= 10) {
    // Verifica se há cookie suficientes
    cookie -= 10;
    cliques += 0.2; // Aumenta o clique em 0.2 a cada compra
    contadorElemento.textContent = cookie.toFixed(1);
  } else {
    alert("Cookies insuficientes!");
  }
}
// Função para comprar empresário (diminuir 50 cookie e aumentar o incremento em 0.5)
function comprar_empresario() {
  if (cookie >= 50) {
    cookie -= 50;
    incremento += 0.5;
    contadorElemento.textContent = cookie.toFixed(1);
    if (!intervaloAtivo) {
      // Ativa o incremento automático uma vez
      empreendedor();
    }
  } else {
    alert("Cookies insuficientes!");
  }
}

// Função para iniciar o incremento automático com o valor acumulativo
function empreendedor() {
  intervaloAtivo = true; // Marca o incremento como ativo
  setInterval(() => {
    cookie += incremento; // Usa o incremento acumulativo
    contadorElemento.textContent = cookie.toFixed(1); // Mostra com uma casa decimal
  }, 1000); // Intervalo de 1 segundo
}
