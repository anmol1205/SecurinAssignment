public class partA2 {
    public static void main(String[] args) {
        int[][] arr = new int[6][6];
        for (int i = 1; i <= 6; i++) {
            for (int j = 1; j <= 6; j++) {
                arr[i-1][j-1] = i + j;
                System.out.printf("(%d, %d) ", i, j);
            }
            System.out.println();
        }
    }
}
