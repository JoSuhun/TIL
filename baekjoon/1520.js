// https://www.acmicpc.net/problem/1520
// 내리막길
// dp dfs

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, m] = input.shift().split(" ").map(Number);
const board = input.map((v) => v.split(" ").map(Number));

const direct = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
function solution() {
  let dp = Array.from(Array(n), () => Array(m).fill(-1));
  dp[n - 1][m - 1] = 1;

  function dfs(y, x) {
    if (dp[y][x] !== -1) {
      return dp[y][x];
    }
    let count = 0;

    for (let d of direct) {
      let [dy, dx] = [y + d[0], x + d[1]];
      if (dy < 0 || dx < 0 || dy > n - 1 || dx > m - 1) continue;
      if (board[dy][dx] >= board[y][x]) continue;
      if (board[dy][dx] < board[y][x]) {
        count += dfs(dy, dx);
      }
    }
    dp[y][x] = count;
    return count;
  }
  console.log(dfs(0, 0));
}

solution();
