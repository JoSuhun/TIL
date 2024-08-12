// https://www.acmicpc.net/problem/11404
// 플로이드
// 플로이드 워셜

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const node = Number(input.shift());
const n = Number(input.shift());
const route = input.map((v) => v.split(" ").map(Number));

function solution() {
  const INF = 21e8;
  let dist = Array.from(Array(node), () => Array(node).fill(INF));
  route.forEach(
    ([start, end, cost]) =>
      (dist[start - 1][end - 1] = Math.min(dist[start - 1][end - 1], cost))
  );

  for (let i = 0; i < node; i++) {
    dist[i][i] = 0;
  }

  for (let d = 0; d < node; d++) {
    for (let i = 0; i < node; i++) {
      for (let j = 0; j < node; j++) {
        dist[i][j] = Math.min(dist[i][j], dist[i][d] + dist[d][j]);
      }
    }
  }
  dist.forEach((col) => {
    for (let v in col) {
      if (col[v] == INF) col[v] = 0;
    }
    console.log(...col);
  });
}
solution();
