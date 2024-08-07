// https://www.acmicpc.net/problem/9251
// LCS (최장 공통 부분 수열)
// dp

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const string1 = input.shift();
const string2 = input.shift();

function solution() {
  const n1 = string1.length;
  const n2 = string2.length;
  let dp = Array.from(Array(n1 + 1), () => Array(n2 + 1).fill(0));
  for (let i = 0; i < n1; i++) {
    for (let j = 0; j < n2; j++) {
      if (string1[i] == string2[j]) {
        dp[i + 1][j + 1] = dp[i][j] + 1;
      } else {
        dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
      }
    }
  }
  return dp[n1][n2];
}

console.log(solution());
