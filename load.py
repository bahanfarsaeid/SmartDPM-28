import numpy as np
import os

def load():
    """
    Load the compressed SmartDPM-28 dataset.
    Returns:
        X: numpy array of shape (20024, 28, 28, 1)
        y: numpy array of shape (20024,)
    """
    base = os.path.join(os.path.dirname(__file__), "data")

    X = np.load(os.path.join(base, "X28_compressed.npz"))["X"]
    y = np.load(os.path.join(base, "y_compressed.npz"))["y"]

    return X, y
