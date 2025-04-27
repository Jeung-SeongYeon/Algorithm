import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
    Arrays.sort(people);
    int boat = 0;

    int left = 0;                // 가장 가벼운 사람 인덱스
    int right = people.length - 1; // 가장 무거운 사람 인덱스

    while (left <= right) {
        int person1 = people[right];
        int person2 = people[left];

        if (person1 + person2 <= limit) {
            left++;  // 둘이 같이 탈 수 있음
        }
        // 무거운 사람은 항상 보트에 탑승
        right--;
        boat++;
    }

    return boat;
}
}