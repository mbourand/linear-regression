import sys

sys.path.append('.')

import shared.src.csv_reader as csv_reader

def main():
	thetas = csv_reader.read_csv('resources/thetas.csv')[0]
	if len(thetas) != 2:
		print("Error: Invalid thetas.csv", file=sys.stderr)
		exit(1)
	try:
		thetas = [float(x) for x in thetas]
	except ValueError:
		print("Error: Invalid thetas.csv", file=sys.stderr)
		exit(1)

	while True:
		km = input("Please enter the amount of kilometers: ")
		try:
			km = float(km)
			if km < 0:
				print("Invalid amount of kilometers: ", file=sys.stderr)
				continue
			break
		except ValueError:
			print("Invalid amount of kilometers", file=sys.stderr)
			continue

	print(f"The estimated price for a car with {km} kilometers is {max(round(thetas[0] + thetas[1] * km, 2), 0)}€")

if __name__ == "__main__":
	main()
