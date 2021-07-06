'use strict'

function createElem(tag, className, id){
	const elem = document.createElement(tag);
			elem.className = className;
	if(id !== undefined) elem.id = id;

	return elem;
}

const TRANSITION_RESTART = 300;

// Template of modal window
// const entranceFormTamplate =
// `<div class="form_wrapp close" id = "form_wrapp">
// 	<form class = "entrance__form close" method="POST" id="login_form" action="#">
// 		<input class="entrance-login" type="text" placeholder="Логин" required tabindex="1" autocomplete="false" autofocus>
// 		<input class="entrance-password" type="password" placeholder="Пароль" required tabindex="2" autocomplete="false">
// 		<input class="entrance-button" type="submit"  value="Войти" tabindex="3">
// 	</form>
// </div>`


// test template
const entranceFormTamplate =
`<form class = "entrance__form close" method="POST" id="login_form" action="#">
	<input class="entrance-login" type="text" placeholder="Логин" required tabindex="1" autocomplete="false" autofocus>
	<input class="entrance-password" type="password" placeholder="Пароль" required tabindex="2" autocomplete="false">
	<input class="entrance-button" type="submit"  value="Войти" tabindex="3">
</form>`


const entranceBtn = document.querySelector('#entrance');

// test
// document.querySelector('.container').addEventListener('ckick', ()=> console.log(111))
// document.querySelector('#container-wrapp').addEventListener('ckick', ()=> console.log(111))



entranceBtn.addEventListener('click', ()=>{
	// console.log(111);
	// innet modalWindow template
	// console.log(document.querySelector('.container').innerHTML);
	// document.querySelector('.container').innerHTML += entranceFormTamplate;
	// console.log(document.querySelector('.container').innerHTML);



	const parent = createElem('div', 'form_wrapp close', 'form_wrapp');
			parent.innerHTML = entranceFormTamplate;
	 		document.querySelector('.container').append(parent)


	// set style's for container and window
	setTimeout(()=>{
		const containerWrapp = document.querySelector('#container-wrapp');
				containerWrapp.classList.add('close');
		const formWrapp = document.querySelector('#form_wrapp');
				formWrapp.classList.remove('close');
		const form = document.querySelector('#login_form');
				form.classList.remove('close');


				// add EListner for modal window
				formWrapp.addEventListener('click', resetPage);
		})
})


function resetPage(event){
	if(event.target.className === 'form_wrapp') {
		restart();
	}
}

function restart(){
	const layer = document.querySelector('.form_wrapp');
	const modal = document.querySelector('#login_form');
			layer.classList.add('close');
			modal.classList.add('close');
	setTimeout(()=>{
		const containerWrapp = document.querySelector('#container-wrapp');
				containerWrapp.classList.remove('close');
				layer.remove();
	},
	 TRANSITION_RESTART);
}