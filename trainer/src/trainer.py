def estimate(km, theta0, theta1):
	return theta0 + theta1 * km

def linear_regression(data, train_factor=0.001, iterations=200000):
	theta0 = 0
	theta1 = 0

	for _ in range(iterations):
		sum0 = sum(estimate(row[0], theta0, theta1) - row[1] for row in data)
		sum1 = sum((estimate(row[0], theta0, theta1) - row[1]) * row[0] for row in data)
		theta0 += -train_factor * sum0 / len(data)
		theta1 += -train_factor * sum1 / len(data)

	return theta0, theta1
