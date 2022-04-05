import sys

sys.path.append('.')

import shared.src.csv_reader as csv_reader
import data_validator
import trainer
import matplotlib.pyplot as plt

def main():
	data = csv_reader.read_csv('resources/data.csv')[1:]
	if not data_validator.validate(data):
		print("Error: invalid data", file=sys.stderr)
		exit(1)

	data = data_validator.format_data(data)
	normalized_data = data_validator.normalize_data(data)
	theta0, theta1 = trainer.linear_regression(normalized_data)
	theta0, theta1 = data_validator.denormalize_thetas(theta0, theta1, data, normalized_data, trainer.estimate)

	print(f"Theta 0: {theta0}\nTheta 1: {theta1}\n")

	with open('resources/thetas.csv', 'w+') as thetas_file:
		thetas_file.write(f"{theta0},{theta1}\n")

	plt.ylabel('Price')
	plt.xlabel('Kilometers')
	plt.title('Price vs. Kilometers')
	plt.plot([row[0] for row in data], [row[1] for row in data], 'ro')
	plt.plot([row[0] for row in data], [trainer.estimate(row[0], theta0, theta1) for row in data], 'b')

	plt.show()


if __name__ == "__main__":
    main()
