package com.jainil.test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class KnapsackSolver {
    List<KnapsackItem> solve(int W, List<KnapsackItem> items) {
        int n = items.size();
        int[][] A = new int[n][W];

        for (int j=0; j<W; j++) {
            A[0][j] = 0;
        }

        for (int i = 1; i < n; i++) {
            for (int x = 0; x < W; x++) {
                int v;
                KnapsackItem item = items.get(i);
                if (item.weight > x) {
                   v = A[i-1][x];
                } else {
                    v = Math.max(A[i-1][x], A[i-1][x-item.weight] + item.value);
                }
                A[i][x] = v;
            }
        }

        List<KnapsackItem> solution = new ArrayList<>();
        int x = W-1;
        for (int i = n-1; i > 0; i--) {
            if (A[i][x] != A[i-1][x]) {
                KnapsackItem item = items.get(i);
                solution.add(item);
                x = x - item.weight;
            }
        }
        Collections.reverse(solution);
        return solution;
    }
}

class KnapsackItem {
    static int idCounter = 1;
    int id;
    int value;
    int weight;

    KnapsackItem(int v, int w) {
        this.id = idCounter++;
        this.value = v;
        this.weight = w;
    }
}