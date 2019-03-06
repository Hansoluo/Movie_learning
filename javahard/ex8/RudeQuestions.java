import java.util.Scanner;

public class RudeQuestions {
	public static void main(String[] args) {
		String name;
		int age;
		double weight, income;

		Scanner keyboard = new Scanner(System.in);

		System.out.print("Hello. what is your name? ");
		name = keyboard.next();

		System.out.print("Hi, " + name + "! How old are you? ");
	}
}