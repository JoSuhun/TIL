// https://www.acmicpc.net/problem/2110
// 공유기설치
// 이분탐색

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, c] = input.shift().split(" ").map(Number);
const position = input.map((v) => Number(v));
position.sort((a, b) => a - b);

function possible(distance, router) {
  let now = position[0];
  let count = router - 1;
  for (let i = 1; i < n; i++) {
    if (position[i] - now >= distance) {
      count -= 1;
      now = position[i];
    }
  }
  return count <= 0;
}

function solution() {
  function binarySearch() {
    let first = 0;
    let last = position[n - 1];
    while (first <= last) {
      let mid = Math.floor((last + first) / 2);
      if (possible(mid, c)) {
        first = mid + 1;
      } else {
        last = mid - 1;
      }
    }
    return last;
  }
  console.log(binarySearch());
}

solution();
