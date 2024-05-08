import java.util.Scanner;

public class Catboat {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Catboat Customer Interaction!");
        System.out.print("Please enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "! How can I assist you today?");
        System.out.println("1. Check balance");
        System.out.println("2. Make a payment");
        System.out.println("3. Update account information");
        System.out.println("4. Speak to a representative");
        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();
        switch (choice) {
            case 1:
                System.out.println("Your current balance is $1000.");
                break;
            case 2:
                System.out.println("Please enter the amount to pay:");
                double amount = scanner.nextDouble();
                System.out.println("Payment of $" + amount + " successful.");
                break;
            case 3:
                System.out.println("Account information updated successfully.");
                break;
            case 4:
                System.out.println("Please wait while we connect you to a representative...");
                // Code to connect to a representative would go here
                break;
            default:
                System.out.println("Invalid choice.");
        }
        System.out.println("Thank you for using Catboat Customer Interaction. Have a great day, " + name + "!");
        scanner.close();
    }
}