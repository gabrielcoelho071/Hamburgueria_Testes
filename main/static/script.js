// const checkboxTabela = document.getElementById('checkbox-tabelaIsTrue');
// const endereco = "http://127.0.0.1:5000"
function openNav() {
  document.getElementById("nav").style.width = "100vw";
}

function closeNav() {
  document.getElementById("nav").style.width = "0";
}

// function testeCheckbox(){
//   renderTabela(checkboxTabela.checked);
// }
// // window.addEventListener("DOMContentLoaded", (event) => {
// //   const checkboxTabela = document.getElementById("checkbox-tabelaIsTrue");
// //   checkboxTabela.addEventListener("selectionchange", (event) => {
// //     console.log('checkbox mudouuuu');
// //   })
// // })
// async function renderTabela(valor_) {
//     try {
//       console.log("valor:", valor_);
//       await fetch(`${endereco}/redirectcards/${valor_}`);
        // if (!res.ok) {
        //   console.log(res);
        //   console.log("ressssss");
        //   console.log(res.status);
        //     throw new Error(`Erro HTTP ${res.status}`);
        // }
        // console.log("res jsonnnnn");
        // console.log(await res.json());

//     } catch (err) {
//         console.log(err.message ?? 'Falha ao buscar dados');
//     }
// }