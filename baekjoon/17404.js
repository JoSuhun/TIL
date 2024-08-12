// https://www.acmicpc.net/problem/17404
// RGB거리 2
// dp
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const house = input.map((v) => v.split(" ").map(Number));

function solution() {
  let answer = [];
  let start = 0;
  let INF = 21e8;
  while (start < 3) {
    let house_copy = JSON.parse(JSON.stringify(house));
    house_copy[1][start] = INF;
    for (let i = 1; i < n; i++) {
      if (i == 1) {
        house_copy[1][0] += house_copy[0][start];
        house_copy[1][1] += house_copy[0][start];
        house_copy[1][2] += house_copy[0][start];
      } else {
        house_copy[i][0] += Math.min(
          house_copy[i - 1][1],
          house_copy[i - 1][2]
        );
        house_copy[i][1] += Math.min(
          house_copy[i - 1][0],
          house_copy[i - 1][2]
        );
        house_copy[i][2] += Math.min(
          house_copy[i - 1][1],
          house_copy[i - 1][0]
        );
      }
    }
    for (let i = 0; i < 3; i++) {
      if (i == start) continue;
      answer.push(house_copy[n - 1][i]);
    }
    start++;
  }
  console.log(Math.min(...answer));
}
solution();
