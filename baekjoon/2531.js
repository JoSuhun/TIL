// https://www.acmicpc.net/problem/2531
// 회전초밥
// 투포인터
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, d, k, c] = input.shift().split(" ").map(Number);
const sushi = input.map(Number);

function solution() {
  function findNumber(start) {
    let cnt = 0;
    let visit = Array(d + 1).fill(0);
    for (let i = start; i < start + k; i++) {
      let now = i;
      if (now >= n) now -= n;
      if (visit[sushi[now]] == 0) {
        visit[sushi[now]]++;
        cnt++;
      }
    }
    if (visit[c] == 0) cnt++;
    return cnt;
  }
  let answer = -1;
  for (let i = 0; i < n; i++) {
    let ret = findNumber(i);
    answer = Math.max(ret, answer);
  }
  console.log(answer);
}
solution();
