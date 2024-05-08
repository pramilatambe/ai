import java.util.Scanner;

public class NQueens {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the chessboard: ");
        int size = scanner.nextInt(); 

        int[] placement = new int[size]; 
        solveNQueens(placement, 0); 
    }

    
    static void solveNQueens(int[] placement, int row) {
        int size = placement.length;

        
        if (row == size) {
            printPlacement(placement);
            return;
        }

        
        for (int col = 0; col < size; col++) {
            
            if (isSafe(placement, row, col)) {
                placement[row] = col; 
                solveNQueens(placement, row + 1); 
            }
        }
    }

   
    static boolean isSafe(int[] placement, int row, int col) {
       
        for (int prevRow = 0; prevRow < row; prevRow++) {
            
            if (placement[prevRow] == col || Math.abs(placement[prevRow] - col) == row - prevRow) {
                return false; 
            }
        }
        return true; 
    }

    
    static void printPlacement(int[] placement) {
        for (int col : placement) {
            System.out.print(col + " "); 
        }
        System.out.println(); 
    }
}