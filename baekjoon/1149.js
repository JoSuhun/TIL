// https://www.acmicpc.net/problem/1149
// RGB거리
// dp
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const house = input.map((v) => v.split(" ").map(Number));

function solution() {
  for (let i = 1; i < house.length; i++) {
    house[i][0] += Math.min(house[i - 1][1], house[i - 1][2]);
    house[i][1] += Math.min(house[i - 1][0], house[i - 1][2]);
    house[i][2] += Math.min(house[i - 1][0], house[i - 1][1]);
  }
  console.log(Math.min(...house.pop()));
}

solution();
