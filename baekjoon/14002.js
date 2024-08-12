// https://www.acmicpc.net/problem/14002
// 가장 긴 증가하는 부분 수열 4
// dp

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const numbers = input.shift().split(" ").map(Number);

function solution() {
  let dp = new Array(n).fill(1);
  let check = new Array(n).fill(-1);
  let maxLength = -1;

  for (let i = 0; i < n; i++) {
    let target = numbers[i];
    for (let j = 0; j < i; j++) {
      let value = numbers[j];
      if (target > value) {
        if (dp[i] < dp[j] + 1) {
          dp[i] = dp[j] + 1;
          check[i] = j;
        }
      }
    }
  }

  maxLength = Math.max(...dp);
  let maxIndex = dp.indexOf(maxLength);
  let answer = [];
  while (check[maxIndex] >= 0) {
    answer.unshift(numbers[maxIndex]);
    maxIndex = check[maxIndex];
  }
  answer.unshift(numbers[maxIndex]);

  console.log(maxLength);
  console.log(...answer);
}

solution();
