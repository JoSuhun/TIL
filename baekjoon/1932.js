// https://www.acmicpc.net/problem/1932
// 정수 삼각형
// dp

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const triangles = input.map((v) => v.split(" ").map(Number));

function solution() {
  let dp = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
  dp[1][1] = triangles[0][0];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i + 1; j++) {
      dp[i + 1][j + 1] = Math.max(
        dp[i][j] + triangles[i][j],
        dp[i][j + 1] + triangles[i][j]
      );
    }
  }
  return Math.max(...dp[n]);
}

console.log(solution());
