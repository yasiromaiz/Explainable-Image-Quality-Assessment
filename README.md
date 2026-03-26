# 🧠 Explainable Image Quality Assessment (XAI + Vision-Language)

An AI-powered system that evaluates image quality and provides **human-readable explanations** using a hybrid approach combining:

- Deep Learning (CNN)
- Feature Engineering
- Vision-Language Models (BLIP)
- Explainable AI (XAI)

---

## 🚀 Demo

Upload an image → Get:
- 📊 Quality Score (0–100)
- 🔍 Extracted Features (blur, brightness, contrast)
- 🧾 AI-generated Explanation (human-like reasoning)

---

## 🧠 Key Features

- ✅ Image Quality Prediction using ResNet18
- ✅ Feature Extraction (blur, brightness, contrast)
- ✅ Vision-Language Understanding (BLIP)
- ✅ Explainable AI (rule-based + AI hybrid explanation)
- ✅ Clean Streamlit UI (responsive design)

---

## 🏗️ System Architecture

Image
↓
CNN Model (ResNet18)
↓
Quality Score (0–100)

Image → Feature Extraction → Technical Features

Image → BLIP Model → Caption

Final Output:
Caption + Feature-based Explanation

---

## 📂 Project Structure

Explainable_IQA/
│
├── data/ # Input images
├── models/ # Saved model weights
│ └── iqa_model.pth
│
├── src/
│ ├── model.py # CNN model
│ ├── train.py # Training pipeline
│ ├── inference.py # Prediction logic
│ ├── features.py # Feature extraction
│ ├── explainer.py # Rule-based explanation
│ ├── vlm_explainer.py # BLIP (Vision-Language)
│
├── app.py # Streamlit UI
├── requirements.txt
└── README.md

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/Explainable-Image-Quality-Assessment.git
cd Explainable-Image-Quality-Assessment

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

▶️ Run the App

streamlit run app.py

🧪 Model Details
Backbone: ResNet18 (Pretrained)
Output: Quality score scaled to 0–100
Activation: Sigmoid (normalized output)
🤖 Vision-Language Model
Model: BLIP (Salesforce)
Purpose: Generate natural language understanding of images
🧠 Explainability Approach

Hybrid explanation system:

1. Visual Caption (BLIP)
2. Technical Analysis (features)
3. Final Combined Explanation

🔥 Future Improvements

 Train on real dataset (KonIQ-10k)
 Add image enhancement suggestions
 Compare multiple images
 Deploy on cloud (Streamlit Cloud)
 Use advanced multimodal models (LLaVA)

🎯 Use Cases

Image quality assessment systems
Photography tools
Surveillance systems
AI explainability research
Computer vision pipelines

👨‍💻 Author

Yasir Omaiz

⭐ If you found this useful

Give this repo a ⭐ and share!