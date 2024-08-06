// https://www.acmicpc.net/problem/2638
// 치즈
// bfs

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [n, m] = input.shift().split(" ").map(Number);
let board = input.map((v) => v.split(" ").map(Number));

function bfs() {
  const direct = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let visit = Array.from(Array(n), () => Array(m).fill(0));
  let q = [[0, 0]];
  visit[0][0] = 1;
  while (q.length > 0) {
    let [nowy, nowx] = q.shift();
    for (let d of direct) {
      let [dy, dx] = [nowy + d[0], nowx + d[1]];
      if (dy < 0 || dx < 0 || dy >= n || dx >= m) continue;
      if (visit[dy][dx] == 1) continue;
      if (board[dy][dx] == 0) {
        visit[dy][dx] = 1;
        q.push([dy, dx]);
      } else {
        board[dy][dx]++;
      }
    }
  }
}

function melting() {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] > 2) {
        board[i][j] = 0;
      } else if (board[i][j] > 0 && board[i][j] <= 2) {
        board[i][j] = 1;
      }
    }
  }
}

function possible() {
  let cheese = 0;
  for (let c of board) {
    if (c.some((item) => item == 1)) cheese++;
  }
  if (cheese == 0) {
    return false;
  } else {
    return true;
  }
}

function solution() {
  let answer = 0;
  while (true) {
    bfs();
    melting();
    answer++;
    if (!possible()) break;
  }
  return answer;
}

console.log(solution());
