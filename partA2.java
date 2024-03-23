import java.util.ArrayList;

public class partA2 {
    public static void main(String[] args) {
        int faces = 6;
        ArrayList<ArrayList<Integer>> dist = new ArrayList<>();

        for (int i = 1; i <= faces; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 1; j <= faces; j++) {
                row.add(i + j);
            }
            dist.add(row);
        }

        System.out.println("Distribution of all possible combinations:");
        
        for (int i = 0; i < dist.size(); i++) {
            ArrayList<Integer> row = dist.get(i);
            System.out.println(row);
        }
    }
}
