class SecondaryDriver extends Thread {
    private int []array;
    private Secondary s;

    public  SecondaryDriver(int []a) {
	this.array=a;
	s=new Secondary();
	System.loadLibrary("Secondary");
    }

    public void run() {
	try {
	    s.sort(array);
	}
	catch (ThreadDeath td) {
	    throw new ThreadDeath();
	}
    }

    public double getMemAccess() {
	return s.getMemAccess();
    }

    public String toString() {
	return "Secondary variant";
    }
}
