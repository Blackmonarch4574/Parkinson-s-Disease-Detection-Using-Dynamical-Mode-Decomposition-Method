# Parkinson-s-Disease-Detection-Using-Dynamical-Mode-Decomposition-Method
Developed a non-invasive Parkinson’s Disease detection system using speech analysis and HODMD for advanced feature extraction. Compared with MFCC, the model achieved ~90% accuracy using Random Forest, effectively capturing complex speech patterns for early diagnosis and scalable healthcare applications.

## Overview

Early detection of Parkinson’s Disease (PD) is essential for effective treatment and management. Traditional diagnostic methods are often invasive, expensive, and require specialised clinical infrastructure. Speech-based analysis offers a promising non-invasive alternative, as PD patients exhibit subtle vocal impairments.

This project proposes a novel approach using Higher Order Dynamic Mode Decomposition (HODMD) for extracting dynamic features from speech signals. By capturing complex temporal patterns in voice recordings, the system enables accurate classification of individuals into PD and healthy categories using machine learning techniques.

## Key Features
HODMD-Based Feature Extraction
Captures nonlinear and temporal dynamics from speech signals more effectively than traditional methods.
Non-Invasive Diagnosis
Uses only voice recordings, enabling remote and cost-effective screening.
Comparative Analysis with MFCC
Evaluates performance against Mel-Frequency Cepstral Coefficients (MFCC).
High Classification Performance
Achieves ~90% accuracy using Random Forest.
Modular & Research-Oriented Codebase
Designed for scalability, experimentation, and integration into healthcare systems.
Model Architecture

The proposed pipeline includes:

Audio Preprocessing
Converts speech signals into structured numerical vectors.
HODMD Feature Extraction
Applies Hankelization and decomposition to extract dynamic modes.
Feature Engineering
Flattens extracted modes into high-dimensional feature vectors.
Machine Learning Classification
Uses models such as Random Forest, SVM, KNN, and Neural Networks.

This architecture effectively captures both temporal and nonlinear speech characteristics associated with Parkinson’s Disease.

## Performance Evaluation

The model was evaluated on speech datasets containing both Parkinson’s patients and healthy individuals. HODMD-based features were compared with MFCC across multiple classifiers.

### Table 1 — Model Accuracy Comparison

(Accuracy in %; best results in bold)
| Method                  | HODMD Accuracy ↑ | MFCC Accuracy ↑ |
|-------------------------|------------------|------------------|
| Logistic Regression     | 60.86            | 88.47            |
| Decision Tree           | 81.36            | 78.50            |
| Random Forest           | **90.06**        | 88.31            |
| SVM                     | 72.04            | 84.57            |
| K-Nearest Neighbour     | 77.08            | 72.74            |
| Neural Network          | 83.22            | 83.80            |

Model	HODMD Accuracy (%)	MFCC Accuracy (%)
Mean Accuracy	0.8433
Std Deviation	0.0578
The model was trained and evaluated using the Italian Voice and Speech Dataset, which includes speech recordings from Parkinson’s patients and healthy individuals.

The dataset contains controlled recordings of syllables such as “pa” and “ta”, sampled at 16 kHz. These recordings capture variations in speech patterns caused by Parkinson’s Disease, enabling effective feature extraction and classification.
