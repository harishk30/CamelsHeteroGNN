# CamelsHeteroGNN

Predicting the matter density parameter ($\Omega_m$) from CAMELS simulation data using heterogeneous Graph Neural Networks (GNNs).

## Overview

This work implements and compares heterogeneous and homogeneous GNN models for cosmological parameter estimation. The heterogeneous approach leverages different galaxy types and their interactions, potentially improving prediction accuracy when galaxies have limited data available.

## Key Features

- Heterogeneous GNN model for multi-type galaxy interactions
- Homogeneous GNN model for baseline comparison
- Data processing pipeline for CAMELS simulation outputs
- Custom loss functions for cosmological parameter estimation
- Hyperparameter optimization using Optuna
- Evaluation metrics: R^2, mean relative error, chi-square
- Visualization tools for model performance analysis

## Requirements

- Python 3.12
- Jupyter Notebook
- PyTorch
- PyTorch Geometric
- Optuna
- Matplotlib
- NumPy
- Scikit-learn

## Notebook Structure

The notebook is organized into the following sections:

- Data Loading and Preprocessing
- Heterogeneous GNN Model Implementation
- Homogeneous GNN Model Implementation
- Model Training
- Hyperparameter Optimization
- Model Evaluation
Results Visualization

## Model Architecture

- The heterogeneous GNN architecture is designed to capture the complex relationships between different types of galaxies (labeled as A, B, and C) within the cosmic web. This approach aims to improve the accuracy of $\Omega_m$ predictions compared to traditional homogeneous graph representations.
- Both models are implemented using PyTorch Geometric and can be easily trained, evaluated, and compared on CAMELS simulation data.

## Data Processing
- The notebook includes scripts for preprocessing CAMELS simulation data, creating graph structures, and preparing the data for input into the GNN models.
  
## Hyperparameter Optimization
- Optuna is used for hyperparameter tuning, allowing for efficient exploration of the model's parameter space to optimize performance.
  
## Evaluation
The models are evaluated using several metrics:
- R^2 score
- Mean relative error (ε)
- Mean Squared Error (MSE)
- Chi-square (χ²)
