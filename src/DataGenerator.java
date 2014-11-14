import java.io.*;
import java.util.Random;

public class DataGenerator {
    public static void main(String []args) {
	String filename;
	int num_ints;
	Writer out;
	Random r=new Random();
	try {
	    filename=args[0];
	    num_ints=Integer.valueOf(args[1]);
	} catch (Exception e) {
	    System.out.println("Usage: DataGenerator [filename] [amount]");
	    return;
	}

	try {
	    out=new FileWriter(filename);
	    for (int i=0;i<num_ints;i++) {
		out.write(String.valueOf(r.nextInt())+"\n");
	    }
	    out.close();
	}
	catch (Exception e) {
	    System.out.println("Error writing to file");
	}
    }
}
