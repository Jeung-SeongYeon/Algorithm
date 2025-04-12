import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    public static int solution(String begin, String target, String[] words) {

        List<String> wordsList = new ArrayList<>();

        for (String word : words) {
            wordsList.add(word);
        }

        wordsList.add(begin);

        Map<String, List<String>> graph = generateGraph(wordsList);
        
        if (!graph.containsKey(begin)) {
            return 0;
        }
        

        int answer = bfs(graph, begin, target);

        return answer;
    }

    public static int bfs(Map<String, List<String>> graph, String begin, String target) {
        Queue<String> queue = new ArrayDeque<String>();
        List<String> visited = new ArrayList<>();
        Queue<Integer> depthQueue = new ArrayDeque<Integer>();
        queue.add(begin);
        depthQueue.add(0);
        while (!queue.isEmpty() && !depthQueue.isEmpty()) {
            String current = queue.poll();
            System.out.println(current);
            Integer currentDepth = depthQueue.poll();
            if (current.equals(target)) {
                return currentDepth;
            }
            visited.add(current);
            List<String> nexts = graph.get(current);
            for (String next : nexts) {
                if (!visited.contains(next)) {
                    queue.add(next);
                    depthQueue.add(currentDepth + 1);
                }
            }
        }
        return 0;
    }

    public static Map<String, List<String>> generateGraph(List<String> words){
        Map<String, List<String>> wordsGraph = new HashMap<String, List<String>>();
        for (int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            for (int j = i; j < words.size(); j++) {
                String target = words.get(j);
                if (canChangeWord(word, target)) {
                    setGraph(wordsGraph, word, target);
                }
            }
        }

        return wordsGraph;
    }

    public static void setGraph(Map<String, List<String>> graph, String word, String target) {
        List<String> wordList = graph.get(word);
        if (wordList == null) {
            wordList = new ArrayList<String>();
            graph.put(word, wordList);
        }
        wordList.add(target);

        List<String> targetList = graph.get(target);
        if (targetList == null) {
            targetList = new ArrayList<String>();
            graph.put(target, targetList);
        }
        targetList.add(word);
    }

    public static boolean canChangeWord(String word, String target) {
        String[] words = word.split("");
        String[] targets = target.split("");
        int len = words.length;
        int checkNum = 0;
        for (int i = 0; i < len; i++) {
            if (words[i].equals(targets[i])) {
                checkNum++;
            }
        }
        if (checkNum == targets.length - 1) {
            return true;
        }
        return false;
    }
}
