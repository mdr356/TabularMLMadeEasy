# 📘 Tabular Machine Learning with PyTorch  
**Made Easy for Beginners**  
by **Marc Daniel Registre**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)
[![Build](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/REPO/actions)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO)

Companion code repository for the book **_Tabular Machine Learning with PyTorch — Made Easy for Beginners_**.  
This repository contains runnable notebooks, practical “Try It Yourself” exercises, datasets, and utilities to help you follow along chapter by chapter.

> 📖 **Buy the book** → [Amazon](https://www.amazon.com/dp/B0FV76J3BZ)  
> 🧠 **Learn by doing** — all examples use **real tabular data** and **PyTorch** step-by-step.

---

## 🧭 Table of Contents

| Part | Chapter | Topic |
|------|---------|-------|
| **Part One: Introduction** | 1 | Why Tabular Machine Learning? |
| | 2A | Understanding Your Data |
| | 2B | Preparing Your Data |
| **Part Two: Regression** | 3 | Regression Matters |
| | 4 | From Math to Machines |
| | 5 | Multiple Linear Regression |
| | 6 | Non-Linear Models |
| **Part Three: Inside a Neural Network** | 7 | The Building Block |
| **Part Four: Classification** | 9 | Multi-Class Classification |
| | 10 | Multi-Label Classification |
| **Part Five: Evaluation & Improvement** | 11 | What Is Model Evaluation? |
| | 12 | The Goldilocks Problem |
| **Part Six: Case Studies** | 13 | Predicting Store Sales |
| | 14 | Customer Churn Prediction |
| | 15 | Tabular Deep Learning Extensions |

---

## 🚀 Quick Start

You can run the notebooks either on **Google Colab** (recommended for beginners) or locally.

### ▶️ Option 1: Run on Google Colab

Click the badge below to open the repo in Colab without any installation:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO)

---

### 💻 Option 2: Run Locally with Conda or venv

```bash
# Clone the repository
git clone https://github.com/USERNAME/REPO.git
cd REPO

# (Recommended) Create a conda environment
conda create -n tabular-ml python=3.10
conda activate tabular-ml

# Install dependencies
pip install -r requirements.txt

# Start Jupyter Notebook
jupyter notebook
```

---

## 📂 Repository Structure

```
public-repo/
└── tmlp/
    └── chapter-code/
        ├── chapter-4.ipynb
        ├── chapter-4-tryItYourself.ipynb
        ├── chapter-5.ipynb
        ├── chapter-5-TryItYourself.ipynb
        ├── chapter-6.ipynb
        ├── chapter-8.ipynb
        ├── chapter-9.ipynb
        ├── Chapter-9-TryItYourSelf-Digits.ipynb
        ├── Chapter-9-TryItYourSelf-Wine.ipynb
        ├── Chapter-10.ipynb
        ├── Chapter-10-TryItYourself.ipynb
        ├── Chapter-13.ipynb
        ├── chapter 14 - pytorch tabular.ipynb
        └── chapter 15 - pytorch tabular.ipynb
```

- Each **chapter notebook** corresponds to a chapter in the book.  
- `TryItYourself` notebooks are exercises for hands-on practice.  
- Case study notebooks (Ch. 13–15) showcase **real-world datasets**.

---

## 📝 Datasets

The datasets used in the book are either:
- Synthetic (generated with `scikit-learn`)
- Publicly available (e.g., UCI ML Repository, Kaggle)
- Packaged with the notebooks

Each notebook includes download links or code to generate the dataset automatically. No manual download is required.

---

## 🧠 What You’ll Learn

By working through these notebooks, you will:
- Understand tabular data preprocessing & feature scaling  
- Build regression & classification models using **PyTorch**  
- Interpret metrics such as **MAE**, **R²**, **accuracy**, **F1**, and more  
- Visualize model predictions and errors  
- Implement **regularization (L1/L2)** and **early stopping**  
- Solve real problems such as **sales prediction** and **customer churn**  

---

## 🤝 Contributing

Contributions are welcome!  
Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Common ways to contribute:
- Fix typos or improve explanations in notebooks
- Add new datasets or exercises
- Translate notebooks into other languages
- Report issues or suggest improvements

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## ✍️ Author

**Marc Daniel Registre**  
- 💼 [LinkedIn](https://www.linkedin.com/in/marc-daniel-registre)  
- 🌐 [Github](https://www.github.com/mdr356)  

---

## ⭐ Acknowledgments

Special thanks to:
- The PyTorch community for making deep learning approachable  
- Readers and early testers who provided valuable feedback  
- Educators and mentors who inspire hands-on learning

---

## 🧭 Next Steps

- 📚 Start with **Chapter 1** and work sequentially  
- 📝 Keep a separate notebook for your experiments  
- 🚀 Share your progress on social media with the hashtag **#TabularMLMadeEasy**
