# Customer Tenure Prediction Using a Neural Network

## Overview

This project trains a small neural network to predict whether a customer
has a tenure of **60 months or more** using two input features:

-   `Age`
-   `MonthlyCharges`

The model is implemented with Scikit-learn's `MLPClassifier`.

## Dataset

The script reads a CSV file named `Cleaned_Customers.csv`.

The dataset must contain these columns:

-   `Age`
-   `MonthlyCharges`
-   `tenure`

Rows with missing values in any of these three columns are removed
before training.

## How It Works

1.  **Load the data** from `Cleaned_Customers.csv`.
2.  **Prepare the features and target**:
    -   Features (`X`): `Age` and `MonthlyCharges`
    -   Target (`y`): `1` if `tenure >= 60`, otherwise `0`
3.  **Split the data** into training and testing sets:
    -   80% training data
    -   20% testing data
    -   `random_state=42` for reproducibility
    -   `stratify=y` to preserve the target-class proportions
4.  **Train the neural network** using an `MLPClassifier` with one
    hidden layer containing 5 neurons and a maximum of 1,000 iterations.
5.  **Evaluate the model** by printing:
    -   Predicted labels
    -   Actual labels
    -   Accuracy
    -   Confusion matrix

## Requirements

-   Python 3
-   pandas
-   scikit-learn

Install the required packages:

``` bash
pip install pandas scikit-learn
```

## Project Structure

``` text
project/
├── DeepLearning.py
├── Cleaned_Customers.csv
└── README.md
```

Keep `Cleaned_Customers.csv` in the same directory as `DeepLearning.py`,
or update the CSV path in the script.

## Run the Project

Run the script from the project directory:

``` bash
python DeepLearning.py
```

## Output

The script displays the model's predictions and the corresponding actual
labels, followed by:

-   **Accuracy:** the proportion of test samples classified correctly.
-   **Confusion Matrix:** a table comparing actual and predicted
    classes, with labels ordered as `0` and `1`.

Class meanings:

-   `0`: Customer tenure is less than 60 months.
-   `1`: Customer tenure is 60 months or more.

## Notes

This README describes the current implementation. The script does not
currently include feature scaling, hyperparameter tuning, or saving the
trained model.
