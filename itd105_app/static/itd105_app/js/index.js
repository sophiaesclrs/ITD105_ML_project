let loginForm = document.querySelector('.login-container');

document.querySelector('#login-btn').onclick = () =>{
  loginForm.classList.toggle('active');
}

document.querySelector('#close-btn').onclick = () =>{
  loginForm.classList.remove('active');
}