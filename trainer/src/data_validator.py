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

def denormalize_thetas(theta0, theta1, data, normalized_data, estimate):
	min_price = min(row[1] for row in data)
	max_price = max(row[1] for row in data)

	km0, km1 = data[0][0], data[1][0]
	normalized_km0, normalized_km1 = normalized_data[0][0], normalized_data[1][0]
	normalized_price0, normalized_price1 = estimate(normalized_km0, theta0, theta1), estimate(normalized_km1, theta0, theta1)
	diff = max_price - min_price
	price0 = data[0][1]

	theta0 = (km1 / (km1 - km0)) * (normalized_price0 * diff + min_price - (km0 / km1 * (normalized_price1 * diff + min_price)))
	theta1 = (price0 - theta0) / km0

	return theta0, theta1

def format_data(data):
	if len(data) == 0:
		return data

	copy = [ row.copy() for row in data]
	for i in range(len(data)):
		for j in range(len(data[i])):
			copy[i][j] = int(copy[i][j])

	return copy
