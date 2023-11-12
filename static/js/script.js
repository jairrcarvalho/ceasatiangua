
const dataTB = document.getElementById('p_data')

function preencherTabeJSON(objetoJSON) {
  // Obtém a tabela pelo ID
  var tabela = document.getElementById("consultatb");

  // Verifica se a tabela foi encontrada
  if (tabela === null) {
    console.error("Tabela com ID '" + tabelaId + "' não encontrada.");
    return;
  }

  // Cria o corpo da tabela se ele não existir
  var corpoTabela = tabela.tBodies[0];

  if (corpoTabela === undefined) {
    corpoTabela = document.createElement("tbody");
    tabela.appendChild(corpoTabela);
  }else{
    corpoTabela.innerHTML = "";
  }

  // Preenche a tabela com os dados do objeto JSON
  for (var chave in objetoJSON) {
    var valor = objetoJSON[chave];

    // Cria uma nova linha na tabela
    var linha = corpoTabela.insertRow();

    // Cria duas células para a chave e o valor
    var celulaChave = linha.insertCell(0);
    var celulaValor = linha.insertCell(1);

    // Define o conteúdo das células
    celulaChave.textContent = chave;
    celulaValor.textContent = valor;
  }
}



const items = document.querySelectorAll('ul li');

items.forEach(function(item){
  item.addEventListener('click', function() {

    const liContent = item.textContent;
    document.querySelector('p').innerText = "BUSCANDO POR : " + liContent.toUpperCase();
    var idConculta;
    switch (liContent) {
      case 'Abobrinha':
        idConculta = 'ABOBRINHA ITALIANA CX.20KG';
        break;
      case 'Brócolis':
        idConculta = "BROCOLIS CX.10KG";
        break;
      case 'Berinjela':  
        idConculta ='BERINJELA CX.13KG'
        break;
      case 'Couve Flôr': 
      idConculta ='COUVE-FLÔR CX.10KG' 
        break;
      case 'Chuchu':
        idConculta = 'CHUCHU CX 25 KG'
        break;
      case 'Pimentão 1º':
        idConculta = 'PRIMEIRA CX.12KG' 
        break;
        case 'Tomate cajá 1º':
          idConculta = 'CAJÁ 1° CX.25KG'
          break;
  }
    url = 'https://files.ceasa-ce.com.br/unsima/boletim_diario/boletim.php'
    const enviaDados = {
        conteudo:idConculta,
        url:url
    };


    fetch('/teste', {
        method: 'POST',
        headers:{
            'Content-type':'application/json'
        },
        body:JSON.stringify(enviaDados)
    })
    .then(response => response.text())
    .then(data => {
      var objeto = JSON.parse(data)
      console.log(objeto)
      preencherTabeJSON(objeto[0])
    });
     
    fetch('/data',{
      method:'POST',
      Headers:{
        'Content-type': 'Application/json'
      }
    })
    .then(response => response.text())
    .then(data => {
      dataTB.innerText = 'Tabela do dia :' + data
      
    });
    


    });
});

