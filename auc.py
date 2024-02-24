from sklearn.metrics import auc
import numpy as np
from sklearn.metrics import roc_curve, auc, roc_auc_score
import matplotlib.pyplot as plt

def read_and_sort_numbers(file_path_english, file_path_tagalog):
    try:
        with open(file_path_english, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
        
        labels = np.zeros(len(numbers))
        with open(file_path_tagalog, 'r') as file:
            numbers.extend([float(line.strip()) for line in file.readlines()])
        labels = np.append(labels, np.ones(len(numbers) - len(labels)))

        return numbers, labels
    except FileNotFoundError:
        print(f"The file {file_path_english} or {file_path_tagalog} was not found.")
    except ValueError:
        print("Make sure the file contains only numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

mean_auc = 0
for i in range(1, 10):
    sorted_list, labels = read_and_sort_numbers(f'english{i}.txt', f'middle{i}.txt')
    auc_score = roc_auc_score(labels, sorted_list)
    mean_auc += auc_score

    fpr, tpr, thresholds = roc_curve(labels, sorted_list)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {auc_score:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('1-Specificity (False Positive Rate)')
    plt.ylabel('Sensitivity (True Positive Rate)')
    plt.title(f'Receiver Operating Characteristic (ROC) with r = {i}')
    plt.legend(loc="lower right")
    plt.show()

mean_auc /= 9
print(f"The mean AUC score is {mean_auc:.2f}")