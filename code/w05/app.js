// app.js - 버튼을 누르면 움직이는 페이지

// 1. 인사 횟수를 기억하는 상자(변수)
let count = 0;

// 2. HTML에서 필요한 부분을 이름(id)으로 찾아오기
const helloButton = document.getElementById("hello-button");
const message = document.getElementById("message");
const colorButton = document.getElementById("color-button");

// 3. 인사 버튼을 누르면 할 일
helloButton.addEventListener("click", function () {
  count = count + 1;
  message.textContent = "반가워요! " + count + "번째 인사예요 😊";
});

// 4. 배경색 버튼을 누르면 할 일
const colors = ["#eef3ff", "#fff3bf", "#d3f9d8", "#ffe3e3"];
let colorIndex = 0;

colorButton.addEventListener("click", function () {
  colorIndex = colorIndex + 1;
  if (colorIndex >= colors.length) {
    colorIndex = 0;
  }
  document.body.style.backgroundColor = colors[colorIndex];
});
