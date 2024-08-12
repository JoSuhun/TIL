// https://www.acmicpc.net/problem/1956
// 운동
// 플로이드 워셜
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [v, e] = input.shift().split(" ").map(Number);
const route = input.map((v) => v.split(" ").map(Number));
function solution() {
  const INF = 21e8;
  let dist = Array.from(Array(v), () => Array(v).fill(INF));
  route.forEach(([start, end, cost]) => (dist[start - 1][end - 1] = cost));
  for (let d = 0; d < v; d++) {
    for (let i = 0; i < v; i++) {
      for (let j = 0; j < v; j++) {
        dist[i][j] = Math.min(dist[i][j], dist[i][d] + dist[d][j]);
      }
    }
  }

  let answer = INF;
  for (let i = 0; i < v; i++) {
    answer = Math.min(dist[i][i], answer);
  }

  if (answer == INF) {
    console.log(-1);
  } else {
    console.log(answer);
  }
}

solution();
