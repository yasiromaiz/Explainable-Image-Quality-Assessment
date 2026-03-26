import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os
import random
from src.model import IQAModel

class DummyDataset(Dataset):
    def __init__(self, folder):
        self.folder = folder
        self.images = os.listdir(folder)
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.folder, self.images[idx])
        image = Image.open(img_path).convert("RGB")
        image = self.transform(image)

        score = torch.tensor([random.uniform(0, 100)], dtype=torch.float32)
        return image, score

dataset = DummyDataset("data/")
loader = DataLoader(dataset, batch_size=4, shuffle=True)

model = IQAModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.MSELoss()

for epoch in range(3):
    for imgs, scores in loader:
        preds = model(imgs)
        loss = loss_fn(preds, scores)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.item()}")

os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), "models/iqa_model.pth")