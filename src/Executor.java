import java.util.*;

class Executor extends Thread {
    private Primary p;
    private SecondaryDriver s;
    private AT tester;
    private int timeLimit;
    private double primaryFailure;
    private double secondaryFailure;
    private double probFail;
    private Random rand;
    private int []checkPoint;
    private int []array;

    public Executor(int []a, int timeout, double prob1, double prob2) {
	rand=new Random();
	this.primaryFailure=prob1;
	this.secondaryFailure=prob2;
	this.array=a;
	p=new Primary(array);
	tester=new AT();
	this.timeLimit=timeout;
	checkPoint=a.clone();
    }

    public void run() {
	Timer t=new Timer();
	Watchdog littleDog=new Watchdog(p);
	t.schedule(littleDog,timeLimit);
	p.start();
	try {
	    p.join();
	    t.cancel();
	    probFail=p.getMemAccess()*primaryFailure;
	    double r=rand.nextDouble();
	    if (!tester.verify(array) || inRange(r,0.5,probFail)) {
		System.out.println("Primary failed");
		array=checkPoint.clone();
		System.out.println("Starting secondary.");
		s=new SecondaryDriver(array);
		t=new Timer();
		littleDog=new Watchdog(s);
		t.schedule(littleDog,timeLimit);
		s.start();
		try {
		    s.join();
		    t.cancel();
		    probFail=s.getMemAccess()*secondaryFailure;
		    r=rand.nextDouble();
		    if (!tester.verify(array) || inRange(r,0.5,probFail)) {
			System.out.println("Secondary failed");
			array=checkPoint.clone();
			throw new ThreadDeath();
		    }
		}
		catch (InterruptedException e){}
	    }

	}
	catch (InterruptedException e){}
    }

    public int []getData() {
	return array;
    }

    private boolean inRange(double num, double min, double max) {
	return num>=min && num<=max;
    }

}
