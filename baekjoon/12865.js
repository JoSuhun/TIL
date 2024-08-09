// https://www.acmicpc.net/problem/12865
// 평범한 배낭
// dp

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, k] = input.shift().split(" ").map(Number);
const items = input.map((item) => item.split(" ").map(Number));

function solution() {
  let dp = Array.from(Array(n + 1), () => Array(k + 1).fill(0));
  for (let i = 1; i < n + 1; i++) {
    let w = items[i - 1][0];
    let v = items[i - 1][1];
    for (let j = 1; j < k + 1; j++) {
      if (w <= j) {
        dp[i][j] = Math.max(dp[i - 1][j], v + dp[i - 1][j - w]);
      } else {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }
  console.log(dp[n][k]);
}

solution();
