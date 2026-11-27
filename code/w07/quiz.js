// quiz.js - "나는 어떤 동물일까?" 성격 테스트 (7주차: 결과 카드와 다시 하기 추가)

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

// 1-2. 결과 정보 (객체) - 동물 이름표마다 이모지, 제목, 설명을 적어 둬요.
const results = {
  cat: { emoji: "🐱", title: "느긋한 고양이", desc: "혼자만의 시간을 소중히 여기고, 차분하게 주변을 챙기는 타입이에요." },
  dog: { emoji: "🐶", title: "활발한 강아지", desc: "사람을 좋아하고 일단 부딪혀 보며 배우는 에너지 넘치는 타입이에요." },
  rabbit: { emoji: "🐰", title: "신중한 토끼", desc: "충분히 살펴보고 준비한 뒤 움직이는 꼼꼼한 타입이에요." },
  fox: { emoji: "🦊", title: "재치 있는 여우", desc: "아이디어가 반짝이고 분위기를 이끄는 센스 있는 타입이에요." },
};

// 2. 점수판 (객체) - 동물마다 점수를 따로 기억해요.
let scores = { cat: 0, dog: 0, rabbit: 0, fox: 0 };

// 3. 지금 몇 번째 질문인지 기억하는 변수
let current = 0;

// 4. 화면에서 쓸 부분 찾아오기
const progress = document.getElementById("progress");
const questionText = document.getElementById("question");
const choiceA = document.getElementById("choice-a");
const choiceB = document.getElementById("choice-b");
const quizArea = document.getElementById("quiz-area");
const resultArea = document.getElementById("result-area");
const resultEmoji = document.getElementById("result-emoji");
const resultTitle = document.getElementById("result-title");
const resultDesc = document.getElementById("result-desc");
const restartButton = document.getElementById("restart-button");

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

// 6-2. 결과 카드를 채우는 함수
function showResult() {
  const info = results[pickResult()];
  resultEmoji.textContent = info.emoji;
  resultTitle.textContent = info.title;
  resultDesc.textContent = info.desc;
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
    showResult();
  }
}

choiceA.addEventListener("click", function () {
  choose(questions[current].a);
});
choiceB.addEventListener("click", function () {
  choose(questions[current].b);
});

// 7-2. 다시 하기: 점수와 질문 번호를 처음으로 돌려요.
restartButton.addEventListener("click", function () {
  scores = { cat: 0, dog: 0, rabbit: 0, fox: 0 };
  current = 0;
  resultArea.classList.add("hidden");
  quizArea.classList.remove("hidden");
  showQuestion();
});

// 8. 첫 질문 보여 주기
showQuestion();
