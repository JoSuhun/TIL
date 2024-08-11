// https://www.acmicpc.net/problem/10942
// 팰린드롬?
// dp

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const numbers = input.shift().split(" ").map(Number);
const q = Number(input.shift());

function solution() {
  let dp = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
  for (let i = 1; i < n; i++) {
    dp[i][i] = 1;
    if (numbers[i - 1] == numbers[i]) dp[i][i + 1] = 1;
  }
  dp[n][n] = 1;
  for (let dist = 3; dist < n + 1; dist++) {
    for (let start = 1; start <= n - dist + 1; start++) {
      let end = start + dist - 1;
      if (dp[start + 1][end - 1] && numbers[start - 1] == numbers[end - 1])
        dp[start][end] = 1;
    }
  }

  let answer = [];
  input.map((v) => {
    const [start, end] = v.split(" ").map(Number);
    answer.push(dp[start][end]);
  });
  console.log(answer.join("\n"));
}
solution();
