import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        int sum = 0;
        int boxes = 0;

        Arrays.sort(capacity);

        for (int i : apple){sum+=i;}
        for (int i = capacity.length -1; i>=0; i--){
            if (sum <=0) break;
            sum-= capacity[i];
            boxes++;
        }
        return boxes;
    }

}