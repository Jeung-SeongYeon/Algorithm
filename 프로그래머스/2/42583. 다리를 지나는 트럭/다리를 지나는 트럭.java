import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        Deque<Integer> bridge = new ArrayDeque<>();
        Deque<Integer> truck = new ArrayDeque<>();

        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        for (int i = 0; i < truck_weights.length; i++) {
            truck.add(truck_weights[i]);
        }

        int time = 0;

        Integer currentWeight = 0;
        while (!truck.isEmpty()) {
            currentWeight -= bridge.pollFirst();
            
            Integer nextWeight = truck.getFirst();

            if (currentWeight + nextWeight <= weight) {
                bridge.addLast(truck.pollFirst());

                currentWeight += nextWeight;
            }else{
                bridge.addLast(0);
            }

            time++;
        }

        answer = time + bridge_length;

        return answer;
    }
}
