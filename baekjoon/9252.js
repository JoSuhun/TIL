// https://www.acmicpc.net/problem/9252
// LCS2 (최장 공통 부분 수열)
// dp

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const string1 = input.shift();
const string2 = input.shift();

const n1 = string1.length;
const n2 = string2.length;

function solution() {
  let dp = Array.from(Array(n1 + 1), () => Array(n2 + 1).fill(""));
  for (let i = 0; i < n1; i++) {
    for (let j = 0; j < n2; j++) {
      if (string1[i] == string2[j]) {
        dp[i + 1][j + 1] = dp[i][j] + string1[i];
      } else {
        dp[i][j + 1].length > dp[i + 1][j].length
          ? (dp[i + 1][j + 1] = dp[i][j + 1])
          : (dp[i + 1][j + 1] = dp[i + 1][j]);
      }
    }
  }
  const answer = dp[n1][n2];
  console.log(`${answer.length}\n${answer}`);
}

solution();
