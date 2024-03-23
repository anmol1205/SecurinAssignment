import java.util.Scanner;
public class partA1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of faces in dice: ");
        int faces = input.nextInt();

        System.out.print("Enter total number of dices: ");
        int n = input.nextInt();

        int totalCombinations = (int) Math.pow(faces, n);
        System.out.println("Total combinations are " + totalCombinations);
        
        input.close();
    }
}
