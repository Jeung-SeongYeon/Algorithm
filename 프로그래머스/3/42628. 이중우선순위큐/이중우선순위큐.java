class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {0, 0};
        Tree tree = new Tree();
        for (String operation : operations) {
           String[] commandList = operation.split(" ");
           String command = commandList[0];
           int value = Integer.parseInt(commandList[1]);

           if (command.equals("I")){
               tree.add(value);
            } else{
               tree.remove(value);
           }
        }

        int minValue = tree.getMin();
        int maxValue = tree.getMax();

        answer[0] = maxValue;
        answer[1] = minValue;

        return answer;
    }

    static class Tree {
        Node root;

        public void add(int n) {
            if (root == null) {
                root = new Node(n);
            } else {
                root.add(n);
            }
        }

        public void remove(int n) {
            if (root != null) {
                Node targetNode = root;
                Node prevNode = root;
                if (n == 1){
                    if (root.right == null){
                        root = root.left;
                        return;
                    }
                    while (targetNode.right != null) {
                        prevNode = targetNode;
                        targetNode = targetNode.right;
                    }
                    prevNode.right = null;
                }else{
                    if (root.left == null){
                        root = root.right;
                        return;
                    }
                    while (targetNode.left != null) {
                        prevNode = targetNode;
                        targetNode = targetNode.left;
                    }
                    prevNode.left = null;
                }
            }
        }
        public int getMax(){
            if (root == null){
                return 0;
            }else{
                Node targetNode = root;
                while(targetNode.right != null){
                    targetNode = targetNode.right;
                }
                return targetNode.num;
            }
        }

        public int getMin(){
            if (root == null){
                return 0;
            }else{
                Node targetNode = root;
                while(targetNode.left != null){
                    targetNode = targetNode.left;
                }
                return targetNode.num;
            }
        }
    }

    static class Node {
        int num;
        Node left, right;

        public Node(int num) {
            this.num = num;
        }

        public Node(int num, Node left, Node right) {
            this.num = num;
            this.left = left;
            this.right = right;
        }

        public void add(int n){
            if (n <= this.num) {
                if (this.left == null) {
                    this.left = new Node(n);
                }else{
                    this.left.add(n);
                }
            } else{
                if (this.right == null) {
                    this.right = new Node(n);
                }else{
                    this.right.add(n);
                }
            }
        }
    }
}