// https://www.acmicpc.net/problem/14890
// 경사로
// 구현

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [n, l] = input.shift().split(" ").map(Number);
const board = input.map((v) => v.split(" ").map(Number));

function possible(r, type) {
  let cnt = 1;
  let flag = false;
  let now = 0;
  let next = 0;

  for (let i = 0; i < n - 1; i++) {
    if (!type) {
      now = board[r][i];
      next = board[r][i + 1];
    } else {
      now = board[i][r];
      next = board[i + 1][r];
    }
    if (now == next) cnt++;
    if (Math.abs(next - now) > 1) return false;
    if (next - now == 1) {
      if (cnt < l) return false;
      else if (flag && cnt / l < 2) return false;
      cnt = 1;
      flag = false;
    }
    if (now - next == 1) {
      if (flag && cnt < l) return false;
      flag = true;
      cnt = 1;
    }
  }

  if (flag && cnt < l) return false;
  return true;
}

function solution() {
  let answer = 0;
  for (let k = 0; k < n; k++) {
    if (possible(k, 1)) answer++;
    if (possible(k, 0)) answer++;
  }
  return answer;
}
console.log(solution());
