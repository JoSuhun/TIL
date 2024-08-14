// https://www.acmicpc.net/problem/4179
// 불!
// bfs

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [r, c] = input[0].trim().split(" ").map(Number);
input.shift();
const miro = input.map((v) => v.split(""));
let jihun = [];
let fire = [];

miro.forEach((row, i) => {
  row.forEach((x, j) => {
    if (x == "J") {
      jihun.push([i, j]);
    } else if (x == "F") {
      fire.push([i, j]);
    }
  });
});

function bfs(q, visit) {
  const direct = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  while (q.length > 0) {
    let now = q.shift();
    for (let d of direct) {
      let dy = now[0] + d[0];
      let dx = now[1] + d[1];
      if (dy < 0 || dx < 0 || dy > r - 1 || dx > c - 1) continue;
      if (visit[dy][dx] >= 0) continue;
      if (miro[dy][dx] == "#" || miro[dy][dx] == "F") continue;
      q.push([dy, dx]);
      visit[dy][dx] = visit[now[0]][now[1]] + 1;
    }
  }
}

function solution() {
  let q_J = jihun;
  let q_F = fire;
  let visit_J = JSON.parse(JSON.stringify(miro));
  let visit_F = JSON.parse(JSON.stringify(miro));
  jihun.forEach(([y, x]) => (visit_J[y][x] = 0));
  fire.forEach(([y, x]) => (visit_F[y][x] = 0));
  // visit_J[jihun[0]][jihun[1]] = 0;
  // visit_F[fire[0]][fire[1]] = 0;
  bfs(q_J, visit_J);
  bfs(q_F, visit_F);
  let answer = 10e9;
  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (i == 0 || i == r - 1 || j == 0 || j == c - 1) {
        if (visit_J[i][j] >= 0) {
          if (
            visit_F[i][j] == "." ||
            visit_F[i][j] == "J" ||
            visit_J[i][j] < visit_F[i][j]
          ) {
            answer = Math.min(visit_J[i][j], answer);
          }
        }
      }
    }
  }
  if (answer == 10e9) {
    return "IMPOSSIBLE";
  } else {
    return answer + 1;
  }
}

console.log(solution());
