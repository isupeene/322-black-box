CLASS_PATH=-classpath ./
LIB_PATH=-Djava.library.path=./
J_PATH=./include/
NUM_ELEMS=100 #Number of integers for DataGenerator to make
PRIM_PROB=0 #Probability that the primary will fail
SEC_PROB=0 #Probability that the secondary will fail
IN_FILE=in.txt #Input file for DataSorter, output of DataGenerator
OUT_FILE=out.txt #Output file for Datasorter
TIME_OUT=100 #Thread timeout for watchdog timer

lib:header
	gcc -shared -fpic -o libSecondary.so -I $(J_PATH) -I $(J_PATH)linux/ Secondary.c
header:classes
	javah -jni Secondary
classes:
	javac *.java
build_run:lib
	java $(CLASS_PATH) DataGenerator in.txt $(NUM_ELEMS)
	java $(CLASS_PATH) $(LIB_PATH) DataSorter $(IN_FILE) $(OUT_FILE) $(PRIM_PROB) $(SEC_PROB) $(TIME_OUT)
run:
	java $(CLASS_PATH) DataGenerator in.txt $(NUM_ELEMS)
	java $(CLASS_PATH) $(LIB_PATH) DataSorter $(IN_FILE) $(OUT_FILE) $(PRIM_PROB) $(SEC_PROB) $(TIME_OUT)

clean:
	rm *.class *~ in.txt out.txt libSecondary.so
