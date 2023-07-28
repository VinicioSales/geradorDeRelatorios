let titulo = document.getElementById('titulo')
let buttonLogin = document.getElementById('login')
let inputEmail = document.getElementById('input-email')
let inputSenha = document.getElementById('input-senha')
let buttonRegistrar = document.getElementById('registrar')
let vizualisarSenha = document.getElementById('mostrarSenha')
const modalCarregando = document.getElementsByClassName('modal-carregando')[0];
const esquciSenha = document.getElementById('esqueci-senha')



vizualisarSenha.addEventListener('click', () => {
    if (inputSenha.type === 'password') {
        inputSenha.type = 'text';
        inputConfirmarSenha.type = 'text';
    } else {
        inputSenha.type = 'password';
        inputConfirmarSenha.type = 'password';
    }
})


function validarInputs() {
    if (inputEmail.value !== '' && inputSenha.value !== '') {
        return true;
    } else {
        return false;
    }
}

function abrirModalCarregando(display) {
    modalCarregando.style.display = display;
};

function logar() {
    let validado = validarInputs()
    if (validado){
    abrirModalCarregando('block')
        let dados = {
            'email': inputEmail.value,
            'senha': inputSenha.value
        };
        fetch(`/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        }).then(res => {
            if (!res.ok) {
                console.log('erro')
                throw new Error(`HTTP error! status: ${res.status}`);
            }
            return res.json()
        })
        .then(data => {
            console.log(data)
            if(data.status === 401) {
                abrirModalCarregando('none')
                titulo.setAttribute('style', 'color: #FF3A3A');
                titulo.innerHTML = data.message
                inputEmail.value = '';
                inputSenha.value = '';
                setTimeout(function() {
                    titulo.setAttribute('style', 'color: #fff');
                    titulo.innerHTML = "Log-in";
                }, 2000)
            } else if(data.status !== 200) {
                alert(data.message)
                window.location.href = data.redirect;
            } 
            else if(data.status == 200) {
                window.location.href = data.redirect;
            }
        })
        .catch(error => {
            console.log(error.message);
        });
    } else {
        alert('Preencha todos os campos')
    }
}

buttonLogin.addEventListener('click', (event) => {
    event.preventDefault()
    logar()

})

buttonRegistrar.addEventListener('click', (event) => {
    abrirModalCarregando('block')
    event.preventDefault()
    window.location.href = `/registrar`;
})

esquciSenha.addEventListener('click', (event) => {
    event.preventDefault()
    if (inputEmail.value !== '') {
        abrirModalCarregando('block')
        data = {
            'email': inputEmail.value
        }
        fetch(`/recuperar_senha`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        body: JSON.stringify(data)
        }).then(res => res.json())
        .then(data => {
            abrirModalCarregando('none')
            alert(data.message)
        }).catch(error => {
            console.log(`error: ${error}`);
            alert('Houve um erro ao tentar recuperar a senha');
        })
    } else {
        alert('Informe o e-mail!')
    }
})
