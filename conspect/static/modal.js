'use strict'

function createElem(tag, class_name, id){
	const elem = document.createElement(tag);
			elem.className = class_name;

	if(id !== undefined) elem.id = id;

	return elem;
}

// get target button
const button_save_cons = document.querySelector('#save_cons')
	 	console.log(button_save_cons);
// record template modal window
const template = `<div class="layer" id = 'layer'>
								<div class="modal__window" id='modal_window'>
									<input type="text" class="modal-input" placeholder="Введите название конспекта" id='input_consp_name'>
									<div class="modal-buttons">
										<input type="button" class="button-ok" value="Сохранить" id="button_ok">
										<input type="button" class="button-cancel" value="Отмена" id="button_cancel">
									</div>
								</div>
						</div>`
const transition_modal = 300;





button_save_cons.addEventListener('click', (event)=>{
	const parent = createElem('div', 'modal', 'modal');
			parent.innerHTML = template;
			document.body.append(parent);
			setTimeout(() => {
				parent.querySelector('#layer').classList.add('open')
				parent.querySelector('#modal_window').classList.add('open')
			},)

			parent.addEventListener('click', clickModal.bind(event))

	// const button_ok = parent.querySelector('#button_ok');
	// const button_cancel = parent.querySelector('button_cancel');
	// 		button_ok.addEventListener('click', saveInput);
	// 		button_cancel.addEventListener('click', deleteModal)
});

function clickModal(event){
	if(event.target.id === 'layer' || event.target.id === 'button_cancel') deleteModal();

	if(event.target.id === 'button_ok'){
		const input = document.querySelector('#input_consp_name');
		if(input.value !== ''){
			fn2(input.value);
			deleteModal();
		}

		input.classList.add('none')

		// }else{
		// }
	}
}


function deleteModal(){
	setTimeout(() => {
		document.querySelector('#layer').classList.remove('open');
		document.querySelector('#modal_window').classList.remove('open');
		setTimeout(()=>document.querySelector('#modal').remove(), transition_modal);
	},)

}