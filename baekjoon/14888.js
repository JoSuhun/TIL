// https://www.acmicpc.net/problem/14888
// 연산자 끼워넣기
// 브루트포스, 백트래킹

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, input_1, input_2] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const numArr = input_1.trim().split(" ").map(Number);
let [plus, minus, mul, div] = input_2.trim().split(" ").map(Number);

let MIN = 1e9;
let MAX = -1e9;
function solution(now, ret) {
  if (now == parseInt(n) - 1) {
    MIN = Math.min(MIN, ret);
    MAX = Math.max(MAX, ret);
    return;
  } else {
    if (plus > 0) {
      plus--;
      solution(now + 1, ret + numArr[now + 1]);
      plus++;
    }
    if (minus > 0) {
      minus--;
      solution(now + 1, ret - numArr[now + 1]);
      minus++;
    }
    if (mul > 0) {
      mul--;
      solution(now + 1, ret * numArr[now + 1]);
      mul++;
    }
    if (div > 0) {
      div--;
      ret < 0
        ? solution(now + 1, Math.floor((ret * -1) / numArr[now + 1]) * -1)
        : solution(now + 1, Math.floor(ret / numArr[now + 1]));
      div++;
    }
  }
}

solution(0, numArr[0]);
console.log(`${MAX}\n${MIN}`);
