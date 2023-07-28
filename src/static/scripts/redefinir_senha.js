let elementoAlerta = document.getElementById('alerta');
let inputToken = document.getElementById('input-token')
let inputSenha = document.querySelector('#input-senha')
let fecharAlertar = document.getElementById('fechar-alerta');
let vizualisarSenha = document.getElementById('mostrarSenha')
let mensagemAlerta = document.getElementById('mensagem-alerta');
const buttonRedefinirSenha = document.getElementById('registrar')
let labelConfirmarSenha = document.querySelector('#labelConfirmarSenha')
let inputConfirmarSenha = document.querySelector('#input-confirmar-senha')
const modalCarregando = document.getElementsByClassName('modal-carregando')[0];


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function mostrarAlerta(message) {
    mensagemAlerta.textContent = message;
    elementoAlerta.style.display = 'block';

    fecharAlertar.addEventListener('click', function() {
        elementoAlerta.style.display = 'none';
    });
}

function abrirModalCarregando(display) {
    modalCarregando.style.display = display;
};

function validarInputs() {
    if (inputSenha.value !== '' && inputConfirmarSenha.value !== '' && inputToken !== '') {
        return true;
    } else {
        return false;
    }
}

inputConfirmarSenha.addEventListener('keyup', () => {
    if(inputConfirmarSenha.value == inputSenha.value){
        labelConfirmarSenha.innerHTML = ''
        labelConfirmarSenha.setAttribute('style', 'color: #FF771E')
    } else {
        labelConfirmarSenha.setAttribute('style', 'color: red')
        labelConfirmarSenha.innerHTML = 'Confirmar Senha *As senhas não conferem'
        inputConfirmarSenha.setAttribute('style', 'border-color: red')
    }
})

vizualisarSenha.addEventListener('click', () => {
    if (inputSenha.type === 'password') {
        inputSenha.type = 'text';
        inputConfirmarSenha.type = 'text';
    } else {
        inputSenha.type = 'password';
        inputConfirmarSenha.type = 'password';
    }
})

function registrar() {
    let validado = validarInputs()
    if(validado) {
    abrirModalCarregando('block')
        let dados = {
            'senha': inputSenha.value,
            'token': inputToken.value
        };
        fetch(`/redefinir_senha`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        }).then(res => {
            return res.json().then(data => {
                return {
                    status: res.status,
                    body: data
                }
            });
        }).then(res => {
            if(res.status === 400) {
                abrirModalCarregando('none')
                alert(res.body.message)
                inputSenha.value = ''
                inputConfirmarSenha.value = ''
            } else if(res.status === 200) {
                abrirModalCarregando('none')
                alert(res.body.message)
                window.location.href = res.body.redirect;
            }
        }).catch(error => {
            console.log(error.message)
        })
    } else {
        alert('Preencha todos os campos')
    }
}

buttonRedefinirSenha.addEventListener('click', (event) => {
    event.preventDefault()
    registrar()
})
