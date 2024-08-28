// https://www.acmicpc.net/problem/13913
// 숨바꼭질 4
// bfs
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [s, d] = input.shift().split(" ").map(Number);

function solution() {
  let board = Array(100001).fill(-1);
  let visited = Array(100001).fill(0);

  function bfs() {
    let q = [];
    q.push(s);
    visited[s] = 1;
    while (q.length > 0) {
      let now = q.shift();
      if (now == d) return;
      for (let next of [now - 1, now + 1, now * 2]) {
        if (next < 0 || next > 100001) continue;
        if (visited[next]) continue;
        visited[next] = visited[now] + 1;
        q.push(next);
        board[next] = now;
      }
    }
  }

  bfs();
  console.log(visited[d] - 1);

  let answer = [];
  let x = d;
  while (x >= 0) {
    answer.unshift(x);
    x = board[x];
  }
  console.log(answer.join(" "));
}
solution();
