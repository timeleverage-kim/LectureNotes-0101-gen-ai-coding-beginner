// quiz.js - "나는 어떤 동물일까?" 성격 테스트 (6주차)

// 1. 질문 목록 (배열) - 각 질문은 선택지 a, b를 가지고, 선택지마다 동물 이름표(type)가 붙어 있어요.
const questions = [
  {
    text: "쉬는 날, 나는?",
    a: { label: "집에서 뒹굴뒹굴 쉰다", type: "cat" },
    b: { label: "친구들과 신나게 논다", type: "dog" },
  },
  {
    text: "처음 보는 사람 앞에서 나는?",
    a: { label: "조용히 상황을 지켜본다", type: "rabbit" },
    b: { label: "먼저 말을 걸어 본다", type: "fox" },
  },
  {
    text: "새로운 게임을 시작할 때 나는?",
    a: { label: "설명서를 꼼꼼히 읽는다", type: "rabbit" },
    b: { label: "일단 해 보면서 배운다", type: "dog" },
  },
  {
    text: "친구가 고민을 말하면 나는?",
    a: { label: "곁에서 조용히 들어 준다", type: "cat" },
    b: { label: "재미있는 해결책을 떠올린다", type: "fox" },
  },
];

// 2. 점수판 (객체) - 동물마다 점수를 따로 기억해요.
const scores = { cat: 0, dog: 0, rabbit: 0, fox: 0 };

// 3. 지금 몇 번째 질문인지 기억하는 변수
let current = 0;

// 4. 화면에서 쓸 부분 찾아오기
const progress = document.getElementById("progress");
const questionText = document.getElementById("question");
const choiceA = document.getElementById("choice-a");
const choiceB = document.getElementById("choice-b");
const quizArea = document.getElementById("quiz-area");
const resultArea = document.getElementById("result-area");
const resultText = document.getElementById("result-text");

// 5. 질문을 화면에 보여 주는 함수
function showQuestion() {
  const q = questions[current];
  progress.textContent = current + 1 + " / " + questions.length;
  questionText.textContent = q.text;
  choiceA.textContent = q.a.label;
  choiceB.textContent = q.b.label;
}

// 6. 가장 점수가 높은 동물을 찾는 함수
function pickResult() {
  let best = "cat";
  for (const type in scores) {
    if (scores[type] > scores[best]) {
      best = type;
    }
  }
  return best;
}

// 7. 선택지를 눌렀을 때 할 일
function choose(option) {
  scores[option.type] = scores[option.type] + 1;
  current = current + 1;

  if (current < questions.length) {
    showQuestion();
  } else {
    quizArea.classList.add("hidden");
    resultArea.classList.remove("hidden");
    resultText.textContent = "당신은 '" + pickResult() + "' 타입이에요!";
  }
}

choiceA.addEventListener("click", function () {
  choose(questions[current].a);
});
choiceB.addEventListener("click", function () {
  choose(questions[current].b);
});

// 8. 첫 질문 보여 주기
showQuestion();
