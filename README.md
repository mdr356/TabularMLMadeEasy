# 📘 Convolutional Neural Networks with PyTorch  
### **Made Easy for Beginners**  
by **Marc Daniel Registre**  
License: MIT | Build | Open in Colab

Companion code repository for **Convolutional Neural Networks with PyTorch — Made Easy for Beginners (Book 2 of the Made Easy Series)**.  
This repo includes runnable notebooks, utilities, datasets, explainability tools, model converters, and **production-ready mobile deployment helpers** used in Chapters 14 and 15.

📖 **Buy the Book → Amazon (Coming Soon)**  
🧠 Learn CNNs by **building real models**, **visualizing how AI sees**, and **deploying your own model to Android & iOS**.

---

# 🧭 Table of Contents (Matches the Book)

## **PART I — Your Machine Learning Foundation**  
*"The expert in anything was once a beginner."*

| Chapter | Topic |
|--------|--------|
| 1 | Book 1 Recap — Tabular ML Essentials |
| — | PyTorch Quick Reference & Cheat Sheets |

---

## **PART II — Understanding Images & CNN Basics**  
*"Every image is a table in disguise — but now, position matters."*

| Chapter | Topic |
|--------|--------|
| 2 | From Loans to Pixels |
| 3 | The RGB Revolution |
| 4A | The Problem with Pixels |
| 4B | Time to Test Our Theory |
| 5 | Convolutional Neural Network |
| 6 | The Pooling Layer |
| 7 | The VGG Blueprint |
| 8 | ResNet — The Skip Connection Revolution |

---

## **PART III — Make Your Model Smarter**  
*"Make your model smarter."*

| Chapter | Topic |
|--------|--------|
| 9 | Transfer Learning |
| 10 | Data Augmentation & Regularization |
| 11 | Visualization (Grad-CAM + Activation Maps) |
| 12 | Object Detection with YOLO |
| 13 | EfficientNet & Modern CNNs |

---

## **PART IV — Real-World Deployment**  
*"Take your model into the real world."*

| Chapter | Topic |
|--------|--------|
| 14 | Deploying to Android |
| 15 | Deploying to iOS |

---

# 🚀 Quick Start

You can run all notebooks on **Google Colab** or locally.

## ▶️ Option 1: Run on Google Colab  
(Coming Soon — each chapter notebook will include a direct “Open in Colab” button)

## 💻 Option 2: Run Locally

```bash
git clone https://github.com/mdr356/CNNMadeEasy.git
cd CNNMadeEasy

conda create -n cnn-made-easy python=3.10
conda activate cnn-made-easy

pip install -r requirements.txt

jupyter notebook
```

---

# 📂 Repository Structure

```
CNNMadeEasy/
├── README.md
├── requirements.txt
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── .gitignore
├── chapter-code/                  ← your notebooks
├── utils/
│   ├── image_utils.py
│   ├── gradcam_utils.py
│   └── lite_rt_converter.py
├── android/
│   └── UniversalAndroidAI.kt
├── ios/
│   └── UniversaliOSAI.swift
├── models/
│   └── mobilenet_universal.tflite  (placeholder in this starter repo)
├── assets/
│   ├── diagrams/
│   └── images/
└── data/
```

---

# 🧱 Deployment Code (Used in Chapters 14 & 15)

This repo includes **full POC implementations** to help beginners deploy real CNNs to their phones.

---

# 📱 Android Deployment Helper — `UniversalAndroidAI.kt`

Used in **Chapter 14 — Deploying to Android (Jetpack Compose, LiteRT)**

```kotlin
class UniversalAndroidAI {
    companion object {
        // Universal model file shipped with your Android app
        const val MODEL_FILE = "mobilenet_universal.tflite"

        fun predictOnAndroid(bitmap: Bitmap): String {
            val model = LiteRTModel.load(MODEL_FILE)
            val input = preprocessForPhone(bitmap)   // convert Bitmap → float tensor
            val results = model.predict(input)
            return "Android: ${interpretResults(results)}"
        }
    }
}
```

This helper shows how to:
- Bundle a `.tflite` model into your app  
- Convert a `Bitmap` into a model-ready tensor  
- Run on-device inference  
- Return a human-readable string for the UI  

---

# 🍎 iOS Deployment Helper — `UniversaliOSAI.swift`

Used in **Chapter 15 — Deploying to iOS (Swift, SwiftUI-compatible)**

```swift
class UniversaliOSAI {
    static func predictOniOS(image: UIImage) -> String {
        let model = try LiteRTModel("mobilenet_universal.tflite")
        let input = preprocessForPhone(image)         // convert UIImage → float tensor
        let results = try model.predict(input)
        return "iOS: \(interpretResults(results))"
    }
}
```

This helper shows how to:
- Load the same `.tflite` model on iOS  
- Convert `UIImage` into tensors  
- Run inference in Swift  
- Keep **one universal model** across Android & iOS  

---

# 📝 Datasets

All datasets load automatically using:

- `torchvision.datasets`  
- Sample images in `assets/images`  
- YOLO demo images for Chapter 12  

No manual downloads required.

---

# 🔍 What You Will Learn

### From ML → Vision
- Why images are 3D tensors  
- How CNNs use RGB channels  
- How convolutions detect edges and patterns  
- Why pooling layers reduce computation  

### Build Real CNN Architectures
- Your first CNN classifier  
- VGG (deep but structured)  
- ResNet (skip connections)  
- MobileNet (optimized for phones)  
- EfficientNet (scaled for performance)  

### Explainability & Visualization
- Activation map visualization  
- Grad-CAM heatmaps  
- Understanding “what your AI sees”  

### Object Detection
- YOLO basics  
- Bounding box predictions  
- Multi-object detection on real images  

### Mobile Deployment
- Exporting PyTorch models to LiteRT/TFLite  
- Packaging `.tflite` inside apps  
- Android + iOS inference  
- End-to-end mobile AI flows  

---

# 🤝 Contributing

See **CONTRIBUTING.md** for full guidelines.

Ways to contribute:
- Improve explanations  
- Add utility functions  
- Add examples or small datasets  
- Fix bugs or typos  

---

# 📄 License

MIT License — see LICENSE.

---

# ✍️ Author

**Marc Daniel Registre**  
🔗 LinkedIn • 🌐 GitHub  

---

# 🧭 Next Steps

📚 Start with Chapter 1  
📸 Try your own images in the notebooks  
🚀 Deploy a model to your phone  
🌐 Share your journey with **#CNNMadeEasy**
# CnnMadeEasy
