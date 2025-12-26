import os
import torch
import torchvision.models as models
import ai_edge_torch

def create_universal_mobile_model():
    """Create ONE .tflite model usable on Android + iOS via LiteRT."""

    print("Step 1: Loading MobileNetV2...")
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT).eval()

    print("Step 2: Preparing sample input...")
    sample_inputs = (torch.randn(1, 3, 224, 224),)

    print("Step 3: Converting with Google AI Edge Torch...")
    edge_model = ai_edge_torch.convert(model, sample_inputs)

    out_dir = "universal_mobile"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mobilenet_universal.tflite")

    print("Step 4: Exporting .tflite...")
    edge_model.export(out_path)

    print("SUCCESS:", out_path)
    print("This ONE file can be used on BOTH Android and iOS with LiteRT.")

if __name__ == "__main__":
    create_universal_mobile_model()
