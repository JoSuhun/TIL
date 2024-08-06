// https://www.acmicpc.net/problem/2467
// 용액
// 이분탐색

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let n = parseInt(input.shift());
let numbers = input.shift().split(" ").map(Number);

function solution() {
  let answer = [];
  if (numbers[n - 1] <= 0) {
    answer = [numbers[n - 2], numbers[n - 1]];
    return answer;
  } else if (numbers[0] >= 0) {
    answer = [numbers[0], numbers[1]];
    return answer;
  } else {
    let MINabs = 2000000000;
    for (let i = 0; i < n - 1; i++) {
      let left = i + 1;
      let right = n - 1;
      while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let sum = numbers[i] + numbers[mid];
        if (Math.abs(sum) < MINabs) {
          MINabs = Math.abs(sum);
          answer = [numbers[i], numbers[mid]];
        }
        if (sum == 0) {
          break;
        } else if (sum > 0) {
          right = mid - 1;
        } else if (sum < 0) {
          left = mid + 1;
        }
      }
    }
    return answer;
  }
}

console.log(...solution());
