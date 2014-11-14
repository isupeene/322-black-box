from subprocess import call
from os import remove

CLASSPATH = "../src/"
LIBRARY_PATH = "../src/"
DATA_GENERATOR = "DataGenerator"
DATA_SORTER = "DataSorter"

DATA_GENERATOR_OUTPUT = "reserved_generator_output.txt"
DATA_SORTER_INPUT = "reserved_sorter_input.txt"
DATA_SORTER_OUTPUT = "reserved_sorter_output.txt"

def invoke_java(program, *args):
	call(
		"java -classpath {} -Djava.library.path={} {} {}"
		.format(CLASSPATH, LIBRARY_PATH, program, " ".join([str(s) for s in args])),
		shell=True
	)

def invoke_data_generator(output_file, number_of_values):
	invoke_java(DATA_GENERATOR, output_file, number_of_values)

def invoke_data_sorter(input_file, output_file, primary_failure_rate, secondary_failure_rate, timeout):
	invoke_java(DATA_SORTER, input_file, output_file, primary_failure_rate, secondary_failure_rate, timeout)

def generate_data(number_of_values):
	invoke_data_generator(DATA_GENERATOR_OUTPUT, number_of_values)
	output_file = open(DATA_GENERATOR_OUTPUT)
	result = [int(x) for x in output_file.readlines()]
	output_file.close()
	remove(DATA_GENERATOR_OUTPUT)
	return result

invoke_data_generator("input.txt", 10)
invoke_data_sorter("input.txt", "output.txt", 1, 1, 10000)
