import java.io.*;
import java.util.*;

class DataSorter {
    public static void main(String []args) {
	String infile;
	String outfile;
	BufferedReader in;
	Writer out;
	double primaryFailure;
	double secondaryFailure;
	int timeLimit;
	int []data;
	ArrayList<Integer> tempData=new ArrayList<Integer>();

	try {
	    infile=args[0];
	    outfile=args[1];
	    primaryFailure=Double.valueOf(args[2]);
	    secondaryFailure=Double.valueOf(args[3]);
	    if (!inRange(primaryFailure,0,1) || !inRange(secondaryFailure,0,1)) {throw new IllegalArgumentException();}
	    timeLimit=Integer.valueOf(args[4]);
	} catch (IllegalArgumentException e) {
	    System.out.println("Failure probabilities must be in the range [0,1]");
	    return;
	}
	catch(Exception e) {
	    System.out.println("Usage: Executor [Input filename] [Output filename]"+
			       " [Primary failure probability] [Secondary failure probability] [Time limit]");
	    System.out.println("Example: Executor in.txt out.txt 0.3 0.5 10");
	    return;
	}

	try {
	    in=new BufferedReader(new FileReader(infile));
	    String line=in.readLine();
	    while(line!=null) {
		tempData.add(Integer.valueOf(line));
		line=in.readLine();
	    }
	    data=new int[tempData.size()];
	    int i=0;
	    for (Integer num:tempData) {
		data[i++]=num;
	    }
	    in.close();
	} catch(Exception e) {
	    System.out.println("Error reading from the file "+infile);
	    return;
	}
	
	Executor exec=new Executor(data,timeLimit,primaryFailure,secondaryFailure);
	exec.start();
	try {
	    exec.join();
	    int []result=exec.getData();
	    AT test=new AT();
	    if (!test.verify(result)) {
		System.out.println("System failed. Sorry");
	    }
	    else {
		try {
		    out=new FileWriter(outfile);
		    for (int num: result) {
			out.write(String.valueOf(num)+"\n");
		    }
		    out.close();
		} catch (Exception e) {
		    System.out.println("Error writing to file "+outfile);
		}
	    }
	}
	catch (InterruptedException e){}
    }

    private static boolean inRange(double num, double min, double max) {
	return num>=min && num<=max;
    }

}

