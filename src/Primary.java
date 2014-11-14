class Primary extends Thread {
    private int []array;
    private double memAccess=0;

    public Primary(int []a) {
	this.array=a;
    }
    
    public void run() {
	try {
	    sort();
	}
	catch (ThreadDeath td) {
	    throw new ThreadDeath();
	}
    }

    public void sort() {
	heapify();
	for (int i=array.length-1;i>1;i--) {
	    memAccess+=5;
	    swap(0,i);
	    bubbleDown(0,i);
	}
	if (array[0]>array[1]) {
	    memAccess+=3;
	    swap(0,1);
	}
    }

    private void heapify() {
	for (int i=0;i<array.length;i++) {
	    memAccess+=5;
	    bubbleUp(i);
	}
    }

    private int parent(int i) {
	memAccess+=3;
	return (i-1)/2;
    }

    private int leftChild(int i) {
	memAccess+=3;
	return (2*i)+1;
    }

    private int rightChild(int i) {
	memAccess+=3;
	return (2*i)+2;
    }

    private void bubbleUp(int position) {
	memAccess+=5;
	if (array[position]>array[parent(position)]) {
	    swap(position,parent(position));
	    bubbleUp(parent(position));
	}
    }

    private void bubbleDown(int position,int end) {
	memAccess+=6;
	int left=leftChild(position);
	int right=rightChild(position);
	if (right<end) {
	    int toSwap=array[left]>array[right]?left:right;
	    if (array[toSwap]>array[position]) {
		swap(position,toSwap);
		bubbleDown(toSwap,end);
	    }
	}
    }

    private void swap(int i1, int i2) {
	memAccess+=5;
	int temp=array[i1];
	array[i1]=array[i2];
	array[i2]=temp;
    }

    public double getMemAccess() {
	return memAccess;
    }

    public String toString() {
	return "Primary Variant";
    }
}
