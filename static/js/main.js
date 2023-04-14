let xhr = new XMLHttpRequest();
const addButton = document.getElementById('add');
const subtractButton = document.getElementById('subtract');
const multiplyButton = document.getElementById('multiply');
const divideButton = document.getElementById('divide');
const answer = document.getElementById('answer');


function getInputValues() {
    number1 = parseInt(document.getElementById('number_1').value);
    number2 = parseInt(document.getElementById('number_2').value);
    return {
        "A": parseInt(number1),
        "B": parseInt(number2)
    }
}


addButton.addEventListener('click', function () {
    xhr.onload = function () {
        let data = JSON.parse(this.response);
        answer.innerText = `Answer: ${data.answer}`;
        if (this.status === 200) {
            answer.style.color = 'green';
        } else {
            answer.style.color = 'red';
        }
    }
    values = getInputValues();
    xhr.open('POST', 'http://127.0.0.1:8000/task_1/add/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(values));
})


subtractButton.addEventListener('click', function () {
    xhr.onload = function () {
        let data = JSON.parse(this.response);
        answer.innerText = `Answer: ${data.answer}`;
        if (this.status === 200) {
            answer.style.color = 'green';
        } else {
            answer.style.color = 'red';
        }
    }
    values = getInputValues();
    xhr.open('POST', 'http://127.0.0.1:8000/task_1/subtract/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(values));
})


multiplyButton.addEventListener('click', function () {
    xhr.onload = function () {
        let data = JSON.parse(this.response);
        answer.innerText = `Answer: ${data.answer}`;
        if (this.status === 200) {
            answer.style.color = 'green';
        } else {
            answer.style.color = 'red';
        }
    }
    values = getInputValues();
    xhr.open('POST', 'http://127.0.0.1:8000/task_1/multiply/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(values));
})


divideButton.addEventListener('click', function () {
    xhr.onload = function () {
        let data = JSON.parse(this.response);
        answer.innerText = `Answer: ${data.answer}`;
        if (this.status === 200) {
            answer.style.color = 'green';
        } else {
            answer.style.color = 'red';
        }
    }
    values = getInputValues();
    xhr.open('POST', 'http://127.0.0.1:8000/task_1/divide/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(values));
})