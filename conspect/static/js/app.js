'use strict'

function createElem(tag, class_name, id){
	const elem = document.createElement(tag);
			elem.className = class_name;
	if(id !== undefined) elem.id = id;

	return elem;
}

const TRANSITION_REMOVE_ELEMS = 300;
const TRANSITION_ADD_ELEMS = 300;
const TRANSITION_REMOVE_BLOCK = 100;
const TRANSITION_ADD_BLOCK = 600;

//! template add_button
const add_template = `<div class="add">
								<span id="add_answer">+ Добавить</span>
								<textarea class = 'user_input' name="" id="" cols="30" rows="1"></textarea>
							</div>`

// First step: get all questions blocks;
//					create order of question's block's;   order:3 (for excample)
//					add EListner for every parent
const question_bloks = document.querySelectorAll('.question_block');
		question_bloks.forEach((elem, order) =>{
			//! template add_button
			elem.innerHTML += add_template;
			elem.setAttribute('order', `${order}`);
			elem.addEventListener('click', checkAnswer);
		})



//! Check new button (add)
const add_blocks = document.querySelectorAll('.add')
		add_blocks.forEach((elem, index)=>{
			elem.setAttribute('parent', index);
		})




function checkAnswer(event){
	if(event.target.classList.contains('answer') || event.target.classList.contains('result')){
		const target = event.target;
		const parent = target.parentNode.parentNode;
		const order = parent.getAttribute('order');
		// console.log({target:target, parent:parent, order:order})

		const opposite_container_class = (parent.getAttribute('class') === 'question_block') ? 'total' : 'questions';
		const opposite_block_class = (parent.getAttribute('class') === 'question_block') ? 'total_block' : 'question_block';
		const opposite_wrapp_class = (parent.getAttribute('class') === 'question_block') ? 'results' : 'answers';
		const opposite_elem_class = (parent.getAttribute('class') === 'question_block') ? 'result' : 'answer';
		// console.log({target:target, parent:parent, order:order, opposite_block: opposite_block_class})

		// true (the opposite parent exist)
		if(checkQuestions(order, opposite_block_class)){
			moveTargetElem(target, opposite_container_class, opposite_wrapp_class, opposite_elem_class, order);
		}

		//false (the opposite parent does't exist)
		if(!checkQuestions(order, opposite_block_class)){
			createQuestionTemplate(target, parent, opposite_container_class, opposite_block_class, opposite_wrapp_class, opposite_elem_class, order)
		}

	}



	//!  Button add elem
	if(event.target.id === 'add_answer'){
		const target_parent = event.target.parentNode;
		const target_textarea = target_parent.querySelector('.user_input');
		const text = target_textarea.value;
		// console.log(event)
				target_textarea.value = "";
				if(text === '') {
					target_textarea.placeholder = 'Введите текст'
				}else{
					const question_block = document.querySelector(`div[order = '${target_parent.getAttribute('parent')}']`)
							console.log(question_block);
					const answers = question_block.querySelector('.answers');
					// console.log(answers)
					const answer = createElem('div', 'answer add_answer');
							// Set delete x
					const del = createElem('span', 'del_answer')
							del.textContent = 'X';
							answer.textContent = text;
							answer.append(del);
							answers.append(answer);
				}

	}

	//! Button del elem
	if(event.target.classList.contains('del_answer')){
		// answer add
		const answer_add_parent = event.target.parentNode;
		// answers
		const answers_parent = answer_add_parent.parentNode;
		const block_parent = answers_parent.parentNode;
				answer_add_parent.remove();
		if(checkParent(answers_parent)){
			cleanContainer(block_parent);
		}

	}
}

function createQuestionTemplate(elem, parent, container_class, block_class, wrapp_class, elem_class, order){
	const opposite_container = document.querySelector(`.${container_class}`);
	const wrapp = elem.parentNode;

	// clone template
	const clone_parent = parent.cloneNode(false);
			clone_parent.className = block_class;
			clone_parent.classList.add('close');
	const clone_title = createElem('h4', 'title_topic')
			clone_title.innerText = parent.querySelector('.title_topic').textContent;
	const clone_wrapp = wrapp.cloneNode(false)
			clone_wrapp.className = wrapp_class;

			//! add button
			if(block_class === 'question_block'){
				const parent = clone_parent.getAttribute('order')
				clone_parent.innerHTML = add_template;
				clone_parent.querySelector('.add').setAttribute('parent', parent);
			}
			clone_parent.prepend(clone_title, clone_wrapp);

	const clone_elem = elem.cloneNode(true);
			clone_elem.className = elem_class;
			clone_elem.classList.add('close')

			elem.classList.add('close');
			clone_wrapp.append(clone_elem);

			clone_parent.addEventListener('click', checkAnswer)
			document.querySelector(`.${container_class}`).append(clone_parent);

	setTimeout(()=>{
		clone_parent.classList.remove('close');
	})

	//delete elem (in outer parent)
	setTimeout(()=> {
		elem.remove();
		if(checkParent(wrapp)) cleanContainer(parent);
	}
	, TRANSITION_REMOVE_ELEMS);

	// add elem (in ipposite parent)
	setTimeout(() =>{
		clone_elem.classList.remove('close');
	})
}




function moveTargetElem(elem, container_class, wrapp_class, elem_class, order){
	const opposite_container = document.querySelector(`.${container_class}`);
	const opposite_parent = opposite_container.querySelector(`div[order = '${order}']`);
	const opposite_wrapp = opposite_parent.querySelector(`.${wrapp_class}`);

	const parent = elem.parentNode.parentNode;
	const wrapp = elem.parentNode;

	const clone_elem = elem.cloneNode(true);
			clone_elem.className = elem_class;
			clone_elem.classList.add('close')

			elem.classList.add('close');
			opposite_wrapp.append(clone_elem);

	// delete elem (in outer parent)
	setTimeout(()=> {
		elem.remove();
		if(checkParent(wrapp)) cleanContainer(parent);
		//! add_button
		// if(opposite_parent.classList.contains('question_block')) console.log(true)
	}
	, TRANSITION_REMOVE_ELEMS);

	// add elem (in opposite parent)
	setTimeout(() =>{
		clone_elem.classList.remove('close');
	})
}






//! Hidden block add
function cleanContainer(parent){
	// .close first layer
	for(let elem of parent.children){
		if(elem.children.length > 0){
			// .close second layer
			for(let i of elem.children){
				i.classList.add('close')
			}
		}
		 elem.classList.add('close');
		}
	parent.classList.add('close');
	setTimeout(()=> parent.remove(), TRANSITION_REMOVE_BLOCK);
}



function checkQuestions(order, class_name){
	const parent_blocks = document.querySelectorAll(`.${class_name}`);
	for(let elem = 0; elem < parent_blocks.length; elem++){
		if(parent_blocks[elem].getAttribute('order') === order) return true;
	}

	return false;
}

function checkParent(wrapp){
	if(wrapp.children.length === 0 ) return true;
	return false;
}






// -------------------------------------------------------------------------------------
// JSON

function getAnswers(input){
	// template for creation json
	const json = {};
			 json.name = input;
	// get parent (left table)
	const total = document.querySelector('#total');
	// get changed answer's
	const target_answers = total.querySelectorAll('[index]');
	// get index's
	const indexes = [];
			target_answers.forEach((answer) => indexes.push(parseInt(answer.getAttribute('index'))));

    console.log(json)
	if(indexes.length !== 0){
		json.answers = indexes;
		return json;
	}
}


function fn2(value) {
	const json = getAnswers(value)

	if(json !== undefined){
		 const requestOptions = {
			  method: 'Post',
			  credentials:'include',
			  headers: {'Content-type':'application/json',
			  "X-CSRFToken": getCookie()
			  },
				body: JSON.stringify(json),

		 };

		 fetch('http://detsad.pythonanywhere.com/api/conspect/create/', requestOptions)
	}
}

function getCookie(){
	let data = document.cookie.split('=');
	const cookie = data[1];
	return cookie
}











































