"""
lambdata-plot_confusion_matrix.
"""
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels


def plot_confusion_matrix(y_true, y_pred):
                labels = unique_labels(y_true)
                columns = [f'Predicted {label}' for label in labels]
                index = [f'Actual {label}' for label in labels]
                df = pd.DataFrame(confusion_matrix(y_true, y_pred),
                                  columns=columns, index=index)

                return sns.heatmap(df, annot=True, fmt='d', cmap='Blues')
