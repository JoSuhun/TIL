// https://www.acmicpc.net/problem/1339
// 단어수학
// 그리디
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const words = input;

function solution() {
  let wordWeights = {};
  let wordNumber = {};
  words.forEach((word) => {
    let len = word.length;
    for (let i = len - 1; i >= 0; i--) {
      if (wordWeights[word[i]]) {
        wordWeights[word[i]] += 10 ** (len - 1 - i);
      } else {
        wordWeights[word[i]] = 10 ** (len - 1 - i);
      }
    }
  });
  const sortedWeights = Object.entries(wordWeights).sort(
    ([, a], [, b]) => b - a
  );
  let k = 9;
  while (sortedWeights.length) {
    let [word, weight] = sortedWeights.shift();
    wordNumber[word] = k;
    k--;
  }

  let answer = 0;

  words.forEach((word) => {
    for (let i = word.length - 1; i >= 0; i--) {
      answer += 10 ** (word.length - 1 - i) * wordNumber[word[i]];
    }
  });

  console.log(answer);
}
solution();
