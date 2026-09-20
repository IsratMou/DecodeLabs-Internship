# Project 2: Data Classification Using AI
### DecodeLabs AI Engineer Industrial Training Kit (Batch 2026)

**Author:** Israt Jahan Mou
**Task:** Build a supervised classification model using a small, well-known dataset.

---

## 1. Overview

This project implements a **K-Nearest Neighbors (KNN)** classifier to predict the species of an iris flower from four physical measurements. It covers the full supervised learning pipeline: data loading, preprocessing, training, and evaluation.

## 2. Dataset

**Iris dataset** (loaded via `sklearn.datasets.load_iris`)

| Property | Value |
|---|---|
| Samples | 150 (balanced) |
| Classes | 3 — *Setosa*, *Versicolor*, *Virginica* (50 each) |
| Features | 4 — Sepal Length, Sepal Width, Petal Length, Petal Width (cm) |

## 3. Methodology

1. **Load & explore** the dataset (shape, class distribution, feature names).
2. **Train-test split** — 80/20, stratified by class, `random_state=42` → 120 training / 30 test samples.
3. **Feature scaling** — `StandardScaler`, fit on the training set only and applied to both sets (prevents data leakage).
4. **Model** — `KNeighborsClassifier` from scikit-learn.
5. **Hyperparameter tuning** — compared K = 1–20 using both a single train/test split and 5-fold cross-validation.
6. **Evaluation** — accuracy, F1-score, confusion matrix, full classification report.

## 4. Results (K = 5)

**Confusion Matrix**

|              | Pred: Setosa | Pred: Versicolor | Pred: Virginica |
|---|---|---|---|
| **Actual: Setosa**     | 10 | 0  | 0 |
| **Actual: Versicolor** | 0  | 10 | 0 |
| **Actual: Virginica**  | 0  | 2  | 8 |

**Classification Report**

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| Setosa | 1.00 | 1.00 | 1.00 | 10 |
| Versicolor | 0.83 | 1.00 | 0.91 | 10 |
| Virginica | 1.00 | 0.80 | 0.89 | 10 |
| **Accuracy** | | | **0.93** | 30 |
| Macro avg | 0.94 | 0.93 | 0.93 | 30 |
| Weighted avg | 0.94 | 0.93 | 0.93 | 30 |

**Overall accuracy: 93.3% (28/30 correct)**

## 5. Hyperparameter Tuning

- A single-split elbow method (K = 1–20) produced a noisy, zigzagging error curve — expected given the small (30-sample) test set, where error can only take values like 1/30 or 2/30.
- **5-fold cross-validation** on the training set gave a smoother, more reliable picture. The highest cross-validated accuracy (~96.7%) occurred at K = 5, 6, 10, and 12, with K = 5–6 forming the most stable plateau.
- **K = 5 was retained** as the final choice — it achieved the best cross-validated accuracy, keeps the model simple, and matches the initial configuration.

## 6. Key Observations

- **Setosa** is linearly separable from the other two species and is classified with perfect precision and recall.
- **Versicolor and Virginica** overlap in feature space (their petal/sepal measurements are close), which is the sole source of error: 2 Virginica samples were misclassified as Versicolor. This lowered Versicolor's precision (0.83) and Virginica's recall (0.80).
- No misclassification involved Setosa, consistent with its known botanical distinctness.

## 7. Conclusion

The KNN model, trained on scaled Iris features with K = 5, achieves 93.3% test accuracy and 96.7% cross-validated accuracy. The full pipeline — load, scale, split, train, tune, evaluate — satisfies the Project 2 requirements (data handling, supervised learning basics, model training) from the DecodeLabs Industrial Training Kit.
