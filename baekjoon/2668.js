// https://www.acmicpc.net/problem/2668
// 숫자고르기
// dfs

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const numbers = [0, ...input.map(Number)];

function solution() {
  function dfs(start, next) {
    if (visit[next] === 0) {
      visit[next] = 1;
      return dfs(start, numbers[next]);
    } else {
      if (start == next) return true;
      else return false;
    }
  }

  let answer = [];
  let visit;
  for (let i = 1; i < n + 1; i++) {
    visit = Array(n + 1).fill(0);
    if (dfs(i, i, visit)) answer.push(i);
  }
  console.log(answer.length);
  console.log(answer.sort((a, b) => a - b).join("\n"));
}
solution();
