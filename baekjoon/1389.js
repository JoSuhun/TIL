// https://www.acmicpc.net/problem/1389
// 케빈 베이컨의 6단계 법칙
// 플로이드 워셜

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, m] = input.shift().split(" ").map(Number);
const route = input.map((v) => v.split(" ").map(Number));

function solution() {
  const INF = 21e8;
  let dist = Array.from(Array(n), () => Array(n).fill(INF));
  route.forEach(([start, end]) => {
    dist[start - 1][end - 1] = 1;
    dist[end - 1][start - 1] = 1;
  });

  for (let d = 0; d < n; d++) {
    for (let i = 0; i < n; i++) {
      dist[i][i] = 0;
      for (let j = 0; j < n; j++) {
        dist[i][j] = Math.min(dist[i][j], dist[i][d] + dist[d][j]);
      }
    }
  }

  let minValue = INF;
  let minIndex = -1;
  dist.forEach((col, index) => {
    if (col.reduce((sum, current) => sum + current) < minValue) {
      minValue = col.reduce((sum, current) => sum + current);
      minIndex = index;
    }
  });
  console.log(minIndex + 1);
}
solution();
