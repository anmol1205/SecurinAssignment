public class partA3 {
    public static void main(String[] args) {
        int faces = 6;

        int[] sumFreq = new int[13]; 
        for (int i = 1; i <= faces; i++) {
            for (int j = 1; j <= faces; j++) {
                int sum = i + j;
                sumFreq[sum]++;
            }
        }
        int totalC = faces * faces;

        System.out.println("Probability of all possible sums occurring:");

        for (int sumValue = 2; sumValue <= 12; sumValue++) {
            double prob = (double) sumFreq[sumValue] / totalC;
            String y = String.format("%.2f", prob);
            System.out.println("Sum: " + sumValue + ", Probability: " + y);
        }
    }
}
