function nova_tarefa() { 
  novaDiv = document.createElement('div');
    novaDiv.className = "container";

    const novaTarefa = document.createElement('p');
    
    const texto = document.getElementById("tarefa").value;
    novaTarefa.append(texto);
    novaDiv.append(novaTarefa);

document.body.append(novaDiv);
}