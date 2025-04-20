import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Map<Integer, List<Integer>> graph = new HashMap<>();

        for (int i = 1; i < N+1; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            String[] input = br.readLine().split(" ");
            int firstNode = Integer.parseInt(input[0]);
            int secondNode = Integer.parseInt(input[1]);

            graph.get(firstNode).add(secondNode);
            graph.get(secondNode).add(firstNode);
        }
        int[] result = bfs(N,1,graph);
        for (int i = 2; i < N+1; i++) {
            System.out.println(result[i]);
        }
    }

    public static int[] bfs(int size, int start, Map<Integer, List<Integer>> graph){
        int[] result = new int[size + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        while (!queue.isEmpty()){
            int current = queue.poll();
            List<Integer> next = graph.get(current);
            for (Integer n : next) {
                if (result[n] == 0 && n!=1) {
                    result[n] = current;
                    queue.add(n);
                }
            }
        }
        return result;
    }
}