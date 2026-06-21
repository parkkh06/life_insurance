import numpy as np

def param_mort_k2013(gender: str) -> np.ndarray:
    """
    Returns Makeham mortality parameters from the K2013 table.

    Parameters
    ----------
    gender : str
        "M" for male, "F" for female.

    Returns
    -------
    np.ndarray
        Array of [alpha, beta, gamma] parameters.
    """
    if gender == "M":
        return np.array([2.671548, -0.172480, 0.001485])
    elif gender == "F":
        return np.array([1.287968, -0.101090, 0.000814])
    else:
        raise ValueError(f"Invalid gender: {gender}")
