import java.util.*;

public class Main {
    public static void main(String[] args){
        int fisrtNum;
        int secondNum;
        int ab;
        
        Scanner AB = new Scanner(System.in);
        fisrtNum = AB.nextInt();
        secondNum = AB.nextInt();
        AB.close();
        ab = fisrtNum+secondNum;

        System.out.println(ab);
    }
}