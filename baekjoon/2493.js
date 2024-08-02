// https://www.acmicpc.net/problem/2493
// 탑
// 스택

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, input] = fs.readFileSync(filePath).toString().trim().split("\n");

const towers = input.trim().split(" ").map(Number);

function solution() {
  const stack = [];
  const answer = new Array(n).fill(0);
  for (let i = 0; i < n; i++) {
    let now = towers[i];
    stack.push([now, i + 1]);

    while (stack.length > 0) {
      const [top, idx] = stack.pop();
      if (top > now) {
        answer[i] = idx;
        stack.push([top, idx]);
        break;
      }
    }

    if (!answer[i]) {
      answer[i] = 0;
    }

    stack.push([now, i + 1]);
  }
  return answer;
}

const ret = solution();
console.log(...ret);
