"""Utilities for exporting PyTorch models to LiteRT / TFLite via ONNX as a demo.

NOTE: In the book, you'll see step-by-step examples.
This file provides simple helper stubs that you can extend.
"""

import torch
import os
from pathlib import Path


def export_to_onnx(model: torch.nn.Module, sample_input: torch.Tensor, export_path: str):
    """Export a PyTorch model to ONNX format."""
    export_path = Path(export_path)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    torch.onnx.export(
        model,
        sample_input,
        export_path,
        input_names=["input"],
        output_names=["output"],
        opset_version=12,
    )
    print(f"Saved ONNX model to {export_path}")


def note_on_litert():
    """Placeholder explaining LiteRT / TFLite conversion.

Actual conversion steps depend on your environment (Python, CLI, or Android Studio).
"""
    print(
        "LiteRT/TFLite conversion is environment-specific. " 
        "Refer to the book's deployment chapters for full commands and screenshots."
    )
