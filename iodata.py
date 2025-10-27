import numpy as np
import scipy
import h5py


def load_checkpoint(filename: str) -> np.ndarray:
    """
    Load a NumPy array from an HDF5 (.h5) file using h5py.
    """
    with h5py.File(f"{filename}.h5", "r") as hf:
        array = hf["data"][:]
    print(f"Checkpoint loaded from {filename}.h5")
    return array