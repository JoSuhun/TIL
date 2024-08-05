// https://www.acmicpc.net/problem/16234
// 인구 이동
// bfs

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [n, l, r] = input[0].trim().split(" ").map(Number);
let people = [];

for (let i = 1; i < input.length; i++) {
  if (input[i] !== "") {
    people.push(input[i].split(" ").map(Number));
  }
}

const directy = [0, 0, 1, -1];
const directx = [1, -1, 0, 0];

function bfs(visited, y, x) {
  const union = [[y, x]];
  const q = [[y, x]];
  while (q.length > 0) {
    const [nowy, nowx] = q.shift();
    for (let k = 0; k < 4; k++) {
      const dy = nowy + directy[k];
      const dx = nowx + directx[k];
      if (dy < 0 || dx < 0 || dy >= n || dx >= n) {
        continue;
      }
      if (visited[dy][dx]) {
        continue;
      }
      if (
        Math.abs(people[nowy][nowx] - people[dy][dx]) >= l &&
        Math.abs(people[nowy][nowx] - people[dy][dx]) <= r
      ) {
        visited[dy][dx] = 1;
        q.push([dy, dx]);
        union.push([dy, dx]);
      }
    }
  }
  return union;
}

function possible(people) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < 4; k++) {
        const dy = i + directy[k];
        const dx = j + directx[k];
        if (dy < 0 || dx < 0 || dy >= n || dx >= n) {
          continue;
        }
        const minus = Math.abs(people[i][j] - people[dy][dx]);
        if (minus >= l && minus <= r) {
          return true;
        }
      }
    }
  }
  return false;
}

function move(union, people) {
  let sum = 0;
  for (let group of union) {
    sum += people[group[0]][group[1]];
  }
  for (let group of union) {
    people[group[0]][group[1]] = Math.floor(sum / union.length);
  }
  return people;
}

function solution() {
  let answer = 0;
  while (true) {
    if (!possible(people)) {
      break;
    } else {
      answer++;
      const visited = Array.from(Array(n), () => Array(n).fill(0));
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          if (visited[i][j]) {
            continue;
          }
          visited[i][j] = 1;
          const ret = bfs(visited, i, j);
          move(ret, people);
        }
      }
    }
  }
  return answer;
}

console.log(solution());
