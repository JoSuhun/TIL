// https://www.acmicpc.net/problem/17951
// 흩날리는 시험지 속에서 내 평점이 느껴진거야
// 이분 탐색

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [input_1, input_2] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [n, k] = input_1.trim().split(" ").map(Number);
const x = input_2.trim().split(" ").map(Number);

function solution() {
  let l = 0;
  let r = x.reduce((curr, total) => curr + total, 0);
  let mid = Math.floor((l + r) / 2);

  while (l <= r) {
    mid = Math.floor((l + r) / 2);
    let group_cnt = 0;
    let group_sum = 0;

    for (const i of x) {
      group_sum += i;
      if (group_sum >= mid) {
        group_cnt++;
        group_sum = 0;
      }
    }
    if (group_cnt >= k) {
      l = mid + 1;
    } else {
      r = mid - 1;
    }
  }
  console.log(r);
}

solution();
