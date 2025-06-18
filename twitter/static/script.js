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

btnFechar.addEventListener('click', (e) => {
    e.preventDefault()
    modalRegister.style.display = 'none'
})

btnOpenLogin.addEventListener('click', (e) => {
    e.preventDefault()
    modalLogin.style.display = 'block'
})

btnFecharLogin.addEventListener('click', (e) => {
    e.preventDefault
    modalLogin.style.display = 'none'
})

btnGoRegister.addEventListener('click', (e) => {
    e.preventDefault()
    modalLogin.style.display = 'none'
    modalRegister.style.display = 'block'
})