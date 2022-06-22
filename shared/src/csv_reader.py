import sys

def read_csv(file_path):
	lines = []
	with open(file_path, 'r') as csv_file:
		lines = csv_file.readlines()
		if len(lines) == 0:
			print("Error: Invalid CSV file", file=sys.stderr)
			exit(1)
		lines = [line.strip() for line in lines]
		lines = [line.split(',') for line in lines]
	return lines
