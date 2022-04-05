# Linear Regression
<img src="https://github.com/mbourand/linear-regression/blob/master/images/illustration.jpg?raw=true">

## Description
This repo contains a simple **linear regression algorithm** predicting the price of a car based on the amount of kilometers it has.

You can use any dataset you want, as long as it is in the correct format.
You can look at the default dataset in ``resources/data.csv``.

## Installation
```
python3 -m venv venv # Creates a virtual environment (optionnal but recommended)
source venv/bin/activate # Activates the virtual environment (Use only if you created the virtual environment)
pip install -r requirements.txt # Installs the required packages
chmod +x *.sh # Adds execution permission for the launching scripts
```

## Usage
```
./trainer.sh # Launches the training script and exports the results to resources/thetas.csv
./finder.sh # Launches the prediction script using the thetas.csv values
```
