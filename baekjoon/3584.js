// https://www.acmicpc.net/problem/3584
// 가장 가까운 공통 조상
// LCA 최소공통조상

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const TC = Number(input.shift());

const inputTestCase = [];

for (let i = 0; i < TC * 2; i += 2) {
  const N = Number(input.shift());
  let nodes = [];
  let target = [];
  for (let i = 0; i < N; i++) {
    nodes.push(input.shift().split(" ").map(Number));
  }
  target = nodes.pop();
  const testCase = {
    N,
    nodes,
    target,
  };
  inputTestCase.push(testCase);
}

function solution() {
  for (let T of inputTestCase) {
    let n = T.N;
    let nodes = T.nodes;
    let target = T.target;
    let tree = new Array(n).fill(-1);
    for (let [y, x] of nodes) {
      tree[x - 1] = y - 1;
    }
    function getDepth(node) {
      let depth = 0;
      while (tree[node] != -1) {
        node = tree[node];
        depth++;
      }
      return depth;
    }
    function LCA(n_x, n_y) {
      let x_depth = getDepth(n_x);
      let y_depth = getDepth(n_y);
      if (x_depth > y_depth)
        return findCommonParent(n_x, n_y, x_depth - y_depth);
      else return findCommonParent(n_y, n_x, y_depth - x_depth);
    }

    function findCommonParent(x, y, diff) {
      while (diff > 0) {
        x = tree[x];
        diff = getDepth(x) - getDepth(y);
      }
      while (x != y) [x, y] = [tree[x], tree[y]];
      return x + 1;
    }

    console.log(LCA(target[0] - 1, target[1] - 1));
  }
}
solution();
