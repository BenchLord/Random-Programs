import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Leet {
    public static void main(String[] args) throws IOException {

        InputStreamReader sr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(sr);


        //ENHANCE: GUI
        System.out.println("==========================");
        System.out.println("|                        |");
        System.out.println("|       BenchLords       |");
        System.out.println("| Mighty Leet Converter! |");
        System.out.println("|                        |");
        System.out.println("==========================\n");
        
        
        boolean running = true; 
        while (running){
            System.out.print("What would you like me to translate? ");
            String input = br.readLine();
            leetitup(input);
            
            System.out.print("Want to translate something else? y/n");
            String answer = br.readLine();
            System.out.print("\n");
            
            if (answer.equals("n"))
            {
                System.out.println("Thanks for using LeetItUp!");
                running = false;
            }
        }
    }

    public static void leetitup(String a)
    {
        //GET THE ORIGINAL STRING WHIPPED 
        //INTO A MORE USABLE FORM
        String lowered = a.toLowerCase();
        char[] listed = lowered.toCharArray();

        //SHOULD PROBABLY BE SWITCH
        //PROBABLY A COMPLETELY BETTER WAY TO DO IT...
        for (char letter : listed)
        {
            if (letter == 'a')
            {
                letter = '4';
            }
            if (letter == 'c')
            {
                letter = '('; 
            }
            if (letter == 'e')
            {
                letter = '3';
            }
            if (letter == 'g')
            {
                letter = '9';
            }
            if (letter == 'i')
            {
                letter = '1';
            }
            if (letter == 'o')
            {
                letter = '0';
            }
            if (letter == 's')
            {
                letter = '$';
            }
            if (letter == 't')
            {
                letter = '7';
            }

            System.out.print(letter);
        }

        System.out.println("\n");
    }
}