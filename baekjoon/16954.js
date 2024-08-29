// https://www.acmicpc.net/problem/16954
// 움직이는 미로탈출
// bfs

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const board = input.map((v) => v.split(""));

function solution() {
  let visitMiro = Array.from(Array(8), () => Array(8).fill(0));
  let q = [];

  function bfs() {
    let direct = [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0],
      [1, 1],
      [1, -1],
      [-1, 1],
      [-1, -1],
    ];
    q.push([7, 0, 1]);

    board.forEach((row, r) => {
      row.forEach((v, c) => {
        if (v == "#") {
          visitMiro[r][c] = 1;
          q.push([r, c, 0]);
        }
      });
    });
    board[7][0] = -1;

    while (q.length > 0) {
      let [nowy, nowx, type] = q.shift();
      if (type) {
        if (nowy == 0 && nowx == 7) return 1;
        if (visitMiro[nowy][nowx] > 0) continue;
        board[nowy][nowx] = -1;
        for (let d of direct) {
          let [nexty, nextx] = [nowy + d[0], nowx + d[1]];
          if (nextx < 0 || nextx > 7 || nexty < 0 || nexty > 7) continue;
          if (board[nexty][nextx] == -1) continue;
          if (visitMiro[nexty][nextx] == 0) q.push([nexty, nextx, type]);
        }
        q.push([nowy, nowx, type]);
      } else {
        visitMiro[nowy][nowx] -= 1;
        if (nowy + 1 > 7) continue;
        visitMiro[nowy + 1][nowx] += 1;
        q.push([nowy + 1, nowx, type]);
      }
    }
    return 0;
  }
  console.log(bfs());
}
solution();
