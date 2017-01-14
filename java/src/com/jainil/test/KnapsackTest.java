package com.jainil.test;

import java.util.ArrayList;
import java.util.List;

public class KnapsackTest {
    public static void main(String[] args) {
        KnapsackSolver solver = new KnapsackSolver();

        List<KnapsackItem> items = new ArrayList<KnapsackItem>();
        items.add(new KnapsackItem(3, 4));
        items.add(new KnapsackItem(2, 3));
        items.add(new KnapsackItem(4, 2));
        items.add(new KnapsackItem(4, 3));

        List<KnapsackItem> sol = solver.solve(6, items);
        for (KnapsackItem item: sol) {
            System.out.println(item.id);
        }
    }
}
