import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner N = new Scanner(System.in);
        String n = N.nextLine();
        String[] array = n.split(" ");
        //System.out.println(Arrays.toString(array));
        N.close();
        int[] nums = Arrays.stream(array).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(nums);
        System.out.println(nums[1]);
    }
}