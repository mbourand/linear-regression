import shared.src.validator as validator

def validate(data):
	try:
		for row in data:
			if len(row) != 2 or not validator.validate_price(int(row[0])) or not validator.validate_km(int(row[1])):
				return False
	except ValueError:
		return False
	return True

def normalize_data(data):
	if len(data) == 0:
		return data

	copy = [row.copy() for row in data]
	for j in range(len(data[0])):
		column = [data[i][j] for i in range(len(data))]
		min_value = min(column)
		max_value = max(column)

		for i in range(len(data)):
			copy[i][j] = (data[i][j] - min_value) / (max_value - min_value)
	return copy

def denormalize(value, min_value, max_value):
    return value * (max_value - min_value) + min_value

def denormalize_thetas(theta0, theta1, data):
	kilometers = [row[0] for row in data]
	prices = [row[1] for row in data]

	spans = [max(col) - min(col) for col in [kilometers, prices]]
	theta1 = theta1 * spans[1] / spans[0]
	theta0 = theta0 * spans[1] + min(prices) - theta1 * min(kilometers)

	return theta0, theta1

def format_data(data):
	if len(data) == 0:
		return data

	copy = [row.copy() for row in data]
	for i in range(len(data)):
		for j in range(len(data[i])):
			copy[i][j] = int(copy[i][j])

	return copy
