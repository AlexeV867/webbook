// Генерация случайных чисел для вопроса
function generateQuestion() {
    const num1 = Math.floor(Math.random() * 10) + 1;
    const num2 = Math.floor(Math.random() * 10) + 1;
    const questionElement = document.getElementById('question');
    questionElement.textContent = `Сколько будет ${num1} × ${num2}?`;
    return { num1, num2 };
}

let currentQuestion = generateQuestion();

// Проверка ответа пользователя
document.getElementById('check-btn').addEventListener('click', () => {
    const userAnswer = parseInt(document.getElementById('answer').value);
    const correctAnswer = currentQuestion.num1 * currentQuestion.num2;
    const resultElement = document.getElementById('result');

    if (userAnswer === correctAnswer) {
        resultElement.textContent = 'Правильно! Молодец!';
        resultElement.style.color = 'green';
    } else {
        resultElement.textContent = `Неправильно. Правильный ответ: ${correctAnswer}`;
        resultElement.style.color = 'red';
    }

    // Генерация нового вопроса
    currentQuestion = generateQuestion();
    document.getElementById('answer').value = '';
});