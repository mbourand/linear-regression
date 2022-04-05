def read_csv(file_path):
	lines = []
	with open(file_path, 'r') as csv_file:
		lines = csv_file.readlines()
		lines = [line.strip() for line in lines]
		lines = [line.split(',') for line in lines]
	return lines
