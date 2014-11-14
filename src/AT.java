class AT {
    public boolean verify(int []a) {
	int biggest=a[0];
	for (int i=1;i<a.length;i++) {
	    if (a[i]<biggest) {return false;}
	    biggest=a[i];
	}
	return true;
    }
}
