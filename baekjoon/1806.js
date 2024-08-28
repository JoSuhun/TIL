// https://www.acmicpc.net/problem/1806
// 부분합
// 투포인터
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, s] = input.shift().split(" ").map(Number);
const numbers = input.shift().split(" ").map(Number);

function solution() {
  let sumList = [0];
  let SUM = 0;
  for (let i = 0; i < n; i++) {
    SUM += numbers[i];
    sumList.push(SUM);
  }
  let start = 0;
  let end = 1;
  let answer = 21e8;
  while (start <= end && end <= n) {
    if (sumList[end] - sumList[start] >= s) {
      answer = Math.min(answer, end - start);
      start++;
    }

    if (sumList[end] - sumList[start] < s) {
      end++;
    }
  }
  if (answer == 21e8) console.log(0);
  else console.log(answer);
}

solution();
