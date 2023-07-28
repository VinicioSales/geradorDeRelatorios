let titulo = document.querySelector('#titulo');
let buttonVoltar = document.getElementById('voltar')
let labelEmail = document.querySelector('#labelEmail')
let labelSenha = document.querySelector('#labelSenha')
let elementoAlerta = document.getElementById('alerta');
let inputEmail = document.getElementById('input-email')
let inputSenha = document.querySelector('#input-senha')
const buttonRegistrar = document.getElementById('registrar')
let fecharAlertar = document.getElementById('fechar-alerta');
let vizualisarSenha = document.getElementById('mostrarSenha')
let mensagemAlerta = document.getElementById('mensagem-alerta');
let labelConfirmarSenha = document.querySelector('#labelConfirmarSenha')
let inputConfirmarSenha = document.querySelector('#input-confirmar-senha')
const modalCarregando = document.getElementsByClassName('modal-carregando')[0];



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
    if (inputEmail.value !== '' && inputSenha.value === inputConfirmarSenha.value) {
        let emailValidado = validarEmail(inputEmail.value)
        if (emailValidado) {
            return true;
        }
    } else {
        return false;
    }
}

function validarEmail(email) {
    // const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const regexEmail = /^[\w.-]+@oitopharma\.com\.br$/;
    return regexEmail.test(email);
}

function validarSenha(senha) {
    const regexSenha = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-=_+{};:,<.>]).{8,}$/;
    return regexSenha.test(senha);

}

inputEmail.addEventListener('keyup', () => {
    let emailValidado = validarEmail(inputEmail.value)
    if(emailValidado){
        labelEmail.innerHTML = ''
        labelEmail.setAttribute('style', 'color: #FF771E')
    } else {
        labelEmail.setAttribute('style', 'color: red')
        labelEmail.innerHTML = 'E-mail não permitido'
        inputEmail.setAttribute('style', 'border-color: red')
    }
})

inputSenha.addEventListener('keyup', () => {
    let senhaValidado = validarSenha(inputSenha.value)
    if(senhaValidado){
        labelSenha.innerHTML = ''
        labelSenha.setAttribute('style', 'color: #FF771E')
    } else {
        labelSenha.setAttribute('style', 'color: red')
        labelSenha.innerHTML = 'Senha não permitida'
        inputSenha.setAttribute('style', 'border-color: red')
    }
})

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
    let emailValidado = validarEmail(inputEmail.value)
    let senhaValidado = validarSenha(inputSenha.value)
    if(validado && emailValidado && senhaValidado) {
        abrirModalCarregando('block')
        let dados = {
            'email': inputEmail.value,
            'senha': inputSenha.value
        };
        fetch(`/registrar`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        }).then(res => {
            if(res.status === 409) {
                console.log(`res: ${res}`)
                abrirModalCarregando('none')
                titulo.setAttribute('style', 'color: #FF3A3A');
                titulo.innerHTML = "E-mail já cadastrado!";
                inputSenha.value = ''
                inputConfirmarSenha.value = ''
                setTimeout(function() {
                    titulo.setAttribute('style', 'color: #fff');
                    titulo.innerHTML = "Registrar";
                }, 3000)
            } else if(res.status === 200) {
                return res.json();
                
            } else{
                console.log("else")
            }
            })
            .then(data => {
                if (data) {
                    abrirModalCarregando('none')
                    alert(data.message)
                    inputSenha.value = '';
                    inputConfirmarSenha.value = '';
                    window.location.href = data.body.redirect;
                }
            })
            .catch(error => {
                console.log(error)
        });
    } else {
        alert('Dados incorretos!')
    }
}

buttonRegistrar.addEventListener('click', (event) => {
    event.preventDefault()
    registrar()
})

buttonVoltar.addEventListener('click', (event) => {
    abrirModalCarregando('block')
    event.preventDefault()
    window.location.href = `/login`;
})

