const buttonSair = document.getElementById('sair-btn')
const inputDataFinal = document.querySelector('#data-final')
const inputDataInicio = document.querySelector('#data-inicio')
const button_enviar_relatorios = document.querySelector('#enviar-relatorios')
const modalCarregando = document.getElementsByClassName('modal-carregando')[0];
const modalRelatorioEnviados = document.getElementById("modal-relatorio-enviado");



function abrirModalCarregando(display) {
    modalCarregando.style.display = display;
};



function abrirModalRelatoriosEnviados() {
    modalRelatorioEnviados.style.display = "block";
};

function fecharModalRelatoriosEnviados() {
    modalRelatorioEnviados.style.display = "none";
}

function validarInputs() {
    if (inputDataInicio.value !== '' && inputDataFinal.value !== '') {
        return true;
    } else {
        return false;
    }
}

modalRelatorioEnviados.addEventListener('click', function (event) {
    if (event.target === modalRelatorioEnviados) {
        fecharModalRelatoriosEnviados();
    }
});


modalRelatorioEnviados.addEventListener('click', function (event) {
    if (event.target === modalRelatorioEnviados) {
        fecharModalRelatoriosEnviados();
    }
});


button_enviar_relatorios.addEventListener('click', (event) => {
    let validado = validarInputs()
    if (validado){
        abrirModalCarregando('block')
        event.preventDefault();
        let dataInicio = inputDataInicio.value;
        let dataFinal = inputDataFinal.value;
        let dados = {
            'dataInicio': dataInicio,
            'dataFinal': dataFinal
        };
        fetch(`/enviar_relatorios`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        }).then(res => {
            if(res.status === 200) {
                abrirModalCarregando('none')
                button_enviar_relatorios.disabled = false;
                button_enviar_relatorios.style.backgound = '#D9D9D9';
                abrirModalRelatoriosEnviados();
            }
            return res.json();
        }).then(dado => {
            console.log(dado.message)
        }).catch(error => {
            console.log(error)
        });
    } else {
        alert('Preencha todos os campos')
    }
});

button_enviar_relatorios.addEventListener('click', (event) => {
    abrirModalCarregando('block')
    event.preventDefault();
    fetch(`/enviar_relatorios`, {
        method: 'GET',
    }).then(res => {
        if(res.status === 200) {
            abrirModalCarregando('none')
            button_enviar_relatorios.disabled = true;
            abrirModalRelatoriosEnviados();
        };
    }).then(dado => {
        console.log(dado.message)
    }).catch(error => {
        console.log(error)
    });
});

buttonSair.addEventListener('click', () => {
    abrirModalCarregando('block')
    fetch(`/logout`, {
        method: 'GET'
    }).then(res => {
        return res.json();
    }).then(data => {
        window.location.href = data.redirect;
    }).catch(error => {
        console.log(error)
    })
})

