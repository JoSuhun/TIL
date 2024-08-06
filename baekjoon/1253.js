// https://www.acmicpc.net/problem/1253
// 좋다
// 이분탐색 투포인터

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = parseInt(input.shift());
const numbers = input.shift().split(" ").map(Number);

function solution() {
  let answer = 0;
  numbers.sort((a, b) => a - b);
  for (let i in numbers) {
    let target = numbers[i];
    let l = 0;
    let r = n - 1;
    while (true) {
      if (i == l) l++;
      if (i == r) r--;
      if (l >= r) break;

      let sum = numbers[l] + numbers[r];

      if (sum == target) {
        answer++;
        break;
      } else if (sum > target) {
        r--;
      } else {
        l++;
      }
    }
  }
  console.log(answer);
}
solution();
