import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        Map<Integer, List<Integer>> graph = new HashMap<>();

        String enter = sc.nextLine();

        for (int i = 0; i < K; i++) {
            String[] network = sc.nextLine().split(" ");

            int firstNode = Integer.parseInt(network[0]);
            int secondNode = Integer.parseInt(network[1]);
            if (!graph.containsKey(firstNode)) {
                graph.put(firstNode, new ArrayList<>());
            }
            if (!graph.containsKey(secondNode)) {
                graph.put(secondNode, new ArrayList<>());
            }

            graph.get(firstNode).add(secondNode);
            graph.get(secondNode).add(firstNode);
        }

        if (!graph.containsKey(1)) {
            System.out.println(0);
        }else {
            System.out.println(dfs(graph));
        }
    }

    public static int dfs(Map<Integer, List<Integer>> graph) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        List<Integer> visited = new ArrayList<>();
        stack.push(1);
        visited.add(1);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            List<Integer> next = graph.get(node);
            for (Integer n : next) {
                if (!visited.contains(n)) {
                    stack.push(n);
                    visited.add(n);
                }
            }
        }

        return visited.size() - 1;
    }
}
