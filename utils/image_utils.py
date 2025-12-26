"""Utility functions for image loading, preprocessing, and visualization."""

from typing import Tuple
from PIL import Image
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as T


def load_image(path: str) -> Image.Image:
    """Load an image from disk as a PIL Image."""
    return Image.open(path).convert("RGB")


def default_transform(image_size: int = 224):
    """Return a basic torchvision transform for CNN models."""
    return T.Compose(
        [
            T.Resize((image_size, image_size)),
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225]),
        ]
    )


def show_image(img: torch.Tensor, title: str = ""):
    """Visualize a tensor image (C, H, W)."""
    img = img.detach().cpu()
    img = img * torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
    img = img + torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
    img = img.clamp(0, 1)
    plt.imshow(img.permute(1, 2, 0))
    plt.axis("off")
    if title:
        plt.title(title)
    plt.show()
