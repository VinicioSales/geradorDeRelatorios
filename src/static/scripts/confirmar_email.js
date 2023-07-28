let inputToken = document.getElementById('input-token')
const buttonConfirmar = document.getElementById('confirmar')
const modalCarregando = document.getElementsByClassName('modal-carregando')[0];



function abrirModalCarregando(display) {
    modalCarregando.style.display = display;
};

function validarInputs() {
    if (inputToken.value !== '') {
        return true;
    } else {
        return false;
    }
}


buttonConfirmar.addEventListener('click', (event) => {
    event.preventDefault();
    let validado = validarInputs();
    console.log(validado);
    if (validado) {
        abrirModalCarregando('block');
        let dados = {
            'token': inputToken.value
        };
        fetch(`/confirmar_email`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        })
        .then(res => {
            if (res.status === 200) {
                return res.json();
            } else if (res.status === 401) {
                throw new Error('Token inválido!');
            } else {
                throw new Error(`HTTP error! status: ${res.status}`);
            }
        })
        .then(data => {
            abrirModalCarregando('none');
            alert(data.message);
            window.location.href = data.redirect;
        })
        .catch(error => {
            abrirModalCarregando('none');
            console.log(`Error: ${error.message}`);
            alert(error.message);
        });
    }
});

