import subprocess
from os import remove
from os import path

CLASSPATH = "../src/"
LIBRARY_PATH = "../src/"
DATA_GENERATOR = "DataGenerator"
DATA_SORTER = "DataSorter"

DATA_GENERATOR_OUTPUT = "reserved_generator_output.txt"
DATA_SORTER_INPUT = "reserved_sorter_input.txt"
DATA_SORTER_OUTPUT = "reserved_sorter_output.txt"


class SortingResult:
	def __init__(self, values, primary_succeeded=True, secondary_succeeded=None):
		self.values = values
		self.primary_succeeded = primary_succeeded
		self.secondary_succeeded = secondary_succeeded

	@staticmethod
	def primary_succeeds(values):
		return SortingResult(values)

	@staticmethod
	def secondary_succeeds(values):
		return SortingResult(values, False, True)

	@staticmethod
	def system_failed():
		return SortingResult(None, False, False)


def invoke_java(program, *args):
	return subprocess.Popen(
		"java -classpath {} -Djava.library.path={} {} {}"
		.format(CLASSPATH, LIBRARY_PATH, program, " ".join([str(s) for s in args])),
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		shell=True
	).communicate()

def invoke_data_generator(output_file, number_of_values):
	return invoke_java(DATA_GENERATOR, output_file, number_of_values)

def invoke_data_sorter(input_file, output_file, primary_failure_rate, secondary_failure_rate, timeout):
	return invoke_java(DATA_SORTER, input_file, output_file, primary_failure_rate, secondary_failure_rate, timeout)

def read_data(filename):
	f = open(filename)
	try:
		return [int(x) for x in f.readlines()]
	finally:
		f.close()

def generate_data(number_of_values):
	try:
		invoke_data_generator(DATA_GENERATOR_OUTPUT, number_of_values)
		return read_data(DATA_GENERATOR_OUTPUT)
	finally:
		remove_silently(DATA_GENERATOR_OUTPUT)

def sort_data(values, primary_failure_rate=0, secondary_failure_rate=0, timeout=100000000):
	try:
		input_file = open(DATA_SORTER_INPUT, "w")
		for value in values:
			input_file.write(str(value) + "\n")
		input_file.close()

		output_text, _ = invoke_data_sorter(DATA_SORTER_INPUT, DATA_SORTER_OUTPUT, primary_failure_rate, secondary_failure_rate, timeout)
		if "System failed" in output_text:
			return SortingResult.system_failed()
		elif "Primary failed" in output_text:
			return SortingResult.secondary_succeeds(read_data(DATA_SORTER_OUTPUT))
		else:
			return SortingResult.primary_succeeds(read_data(DATA_SORTER_OUTPUT))
	finally:
		remove_silently(DATA_SORTER_INPUT)
		remove_silently(DATA_SORTER_OUTPUT)

def generate_and_sort_data(number_of_values, **kwargs):
	return sort_data(generate_data(number_of_values), **kwargs)

def remove_silently(filename):
	try:
		remove(filename)
	except:
		pass

