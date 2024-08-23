# Breast Cancer Classifier

This repository contains code for preprocessing the Winconsin cancer dataset, training models, and assessing their performance using metrics like roc auc curve and confusion matrix.

```
import seaborn as sns
```	

# Overview

Tasks:

- [x] Train models to see which classifier performs best on the Winconsin breast cancer dataset
- [ ] Show performance metrics to user

__Models__
- [x] Logistic regression
- [x] Gaussian Naive bayes
- [x] KNN
- [x] SVM
- [x] Decision Tree
- [x] Random Forest
- [x] Gradient Boosting

__Metrics__
- [x]  confusion matrix
- [x]  roc auc curve

__Tweaks__
- [ ] Hyperparameter tuning

# Getting Started

__Clone the repository__
```
~ git clone https://github.com/rizanB/breast-cancer.git .
```

__Take a look at the notebook__
```
~ my.ipynb
```

__Running with Docker__

1. Build Docker image

```
docker build -t breast-cancer .
```
2. Run a container with the image

```
docker run -p 5000:5000 breast-cancer
```

__Running without Docker__

1. Install required packages
```
pip install -r requirements.txt
```

2. Start Flask server
```
python app.py 
```
__Accessing the application__
Open a browser and visit http://localhost:5000.
