document.addEventListener('DOMContentLoaded', () => {
  const modalRegister = document.getElementById('modal')
  const modalLogin = document.getElementById('modal-login')

  const btnFechar = document.getElementById('close-register')
  const btnOpen = document.getElementById('open-btn')

  const btnOpenLogin = document.getElementById('open-login')
  const btnFecharLogin = document.getElementById('close-login')
  const btnGoRegister = document.getElementById('go-register')

  btnOpen.addEventListener('click', (e) => {
    e.preventDefault()
    modalRegister.style.display = 'block'
  })

  if (btnFechar) {
    btnFechar.addEventListener('click', (e) => {
      e.preventDefault()
      modalRegister.style.display = 'none';
      if (mensagemDiv) mensagemDiv.innerText = '';
    })
  }  

  btnOpenLogin.addEventListener('click', (e) => {
    e.preventDefault()
    modalLogin.style.display = 'block'
  })

  btnFecharLogin.addEventListener('click', (e) => {
    e.preventDefault()
    modalLogin.style.display = 'none'
    if (mensagem) mensagem.innerText = '';
  })

  btnGoRegister.addEventListener('click', (e) => {
    e.preventDefault()
    modalLogin.style.display = 'none'
    modalRegister.style.display = 'block'
  })

  const usernameInput = document.getElementById('registerUsername')
  const emailInput = document.getElementById('registerEmail')
  const passwordInput = document.getElementById('registerPassword')
  const mensagemDiv = document.getElementById('registerMensagem')
  const submitBtn = document.getElementById('registerSubmit')

  function verificarCampo() {
    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const senha = passwordInput.value.trim();
    const MensagemErro = mensagemDiv.textContent === '';

    submitBtn.disabled = !(username && email && senha && MensagemErro);
  }

  async function verificarUsuario(username) {
    const resposta = await fetch(`/verificar_usuario/?username=${encodeURIComponent(username)}`);
    const data = await resposta.json();

    if (data.exists) {
      mensagemDiv.textContent = 'Usuário já existe';
      submitBtn.disabled = true;
    }
    else {
      mensagemDiv.textContent = ''
      verificarCampo()
    }
  } 
  usernameInput.addEventListener('input', () => {
    const username = usernameInput.value.trim();

    if (username) {
      verificarUsuario(username)
    } else {
      mensagemDiv.textContent = '';
      verificarCampo();
    }
  })
  emailInput.addEventListener('input', verificarCampo);
  passwordInput.addEventListener('input', verificarCampo);
})


