import numpy as np
from dataclasses import dataclass
from numpy.typing import ArrayLike


@dataclass
class CPUDelta:
    z: ArrayLike
    wave: ArrayLike
    delta: ArrayLike
    weights: ArrayLike
    dist_c: ArrayLike
    dist_m: ArrayLike

    ra: float
    dec: float
    z_qso: float
    los_id: int
