from sklearn.metrics import auc
import numpy as np
from sklearn.metrics import roc_curve, auc, roc_auc_score
import matplotlib.pyplot as plt

def read(file_path_scores, file_path_identifiers, file_path_labels):
    try:
        with open(file_path_scores, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
        
        with open(file_path_identifiers, 'r') as file:
            identifiers = [int(line.strip()) for line in file.readlines()]
            print(len(np.unique(identifiers)))

        with open(file_path_labels, 'r') as file:
            labels = [int(line.strip()) for line in file.readlines()]
            print(len(labels))

        scores = []
        for i in range(len(identifiers)):
            if i == 0:
                temp_score = []
                current_id = identifiers[i]
                temp_score.append(numbers[i])
            else:
                if identifiers[i] == current_id and i != len(identifiers) - 1:
                    temp_score.append(numbers[i])
                else:
                    mean_score = sum(temp_score) / len(temp_score)
                    scores.append(mean_score)
                    temp_score = []
                    temp_score.append(numbers[i])
                    current_id = identifiers[i]

        return scores, labels
    except FileNotFoundError:
        print(f"The file {file_path_identifiers} or {file_path_scores} was not found.")
    except ValueError:
        print("Make sure the file contains only numbers.")

rs = [2, 3, 7]
parts = [1, 2, 3]
folder = 'snd-cert'

mean_auc = 0
r = 3
part = 1

for part in parts:
    for r in rs:
        scores, labels = read(f'snd_cert7{r}-{part}.txt', f'{folder}-chunks-7-identifiers.{part}.txt', f'{folder}.{part}.labels')
        auc_score = roc_auc_score(labels, scores)
        print(auc_score)

        fpr, tpr, thresholds = roc_curve(labels, sorted_list)

        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {auc_score:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('1-Specificity (False Positive Rate)')
        plt.ylabel('Sensitivity (True Positive Rate)')
        plt.title(f'Receiver Operating Characteristic (ROC) Testing set {part} with r = {r}')
        plt.legend(loc="lower right")
        plt.show()
