import torch
from torchvision import transforms
from PIL import Image
from src.model import IQAModel
from src.features import extract_features
from src.explainer import generate_explanation
from src.vlm_explainer import generate_vlm_explanation


def predict(image_path):
    # Load model
    model = IQAModel()
    model.load_state_dict(torch.load("models/iqa_model.pth"))
    model.eval()

    # Transform
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    # Load image
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    # Prediction
    with torch.no_grad():
        score = model(image).item()*100

    # Feature extraction
    features = extract_features(image_path)

    # Generate explanation (NEW 🔥)
    explanation = generate_explanation(score, features)

    # Return all
    return score, features, explanation