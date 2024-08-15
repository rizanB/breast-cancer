import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_dataset(x):
    dataset = pd.read_csv(x)
    dataset_head = dataset.head()
    print(dataset_head)
    dataset_info = dataset.info()
    print(dataset_info)
        
explore_dataset("data.csv")