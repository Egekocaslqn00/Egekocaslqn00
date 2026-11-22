"""Generic outline of the public case-study method.

This is intentionally data-agnostic. It is not wired to the confidential
internship files and contains no private schema names or operational values.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ValidationResult:
    mape_pct: float
    n_hours: int
    note: str = ""


def mape(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Hourly MAPE for strictly positive demand observations."""
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    if actual.shape != predicted.shape or np.any(actual <= 0):
        raise ValueError("actual and predicted must have equal shape and positive actuals")
    return float(np.mean(np.abs(actual - predicted) / actual) * 100.0)


def build_calendar_features(timestamp: pd.Series) -> pd.DataFrame:
    """Create features that are safe to compute from a local-time index."""
    ts = pd.to_datetime(timestamp)
    return pd.DataFrame({
        "hour": ts.dt.hour,
        "weekday": ts.dt.dayofweek,
        "month": ts.dt.month,
        "is_weekend": (ts.dt.dayofweek >= 5).astype(int),
        "hour_sin": np.sin(2 * np.pi * ts.dt.hour / 24),
        "hour_cos": np.cos(2 * np.pi * ts.dt.hour / 24),
    })


def normalize_peer_load(peer_load: pd.DataFrame, calibration_rows: int) -> pd.DataFrame:
    """Convert peer loads into relative activity signals.

    The caller supplies de-identified peer columns and permissioned data.
    """
    if calibration_rows <= 0 or calibration_rows > len(peer_load):
        raise ValueError("invalid calibration window")
    means = peer_load.iloc[:calibration_rows].mean(axis=0)
    if (means <= 0).any():
        raise ValueError("peer calibration means must be positive")
    return peer_load.divide(means, axis="columns")


def leave_one_building_out_protocol(buildings: dict[str, pd.Series],
                                    calibration_rows: int) -> list[ValidationResult]:
    """Define the evaluation contract without exposing any source data.

    A production implementation would fit the chosen ensemble using all
    remaining peer buildings and score the held-out suffix. This outline keeps
    model fitting out of the public repository because the original inputs are
    confidential.
    """
    if len(buildings) < 3:
        raise ValueError("use at least three permissioned proxy buildings")
    results: list[ValidationResult] = []
    for name, series in buildings.items():
        if len(series) <= calibration_rows:
            raise ValueError(f"{name}: insufficient suffix for holdout")
        results.append(ValidationResult(
            mape_pct=float("nan"),
            n_hours=len(series) - calibration_rows,
            note="fit the fixed ensemble on the other buildings; score this suffix",
        ))
    return results


if __name__ == "__main__":
    print("Generic outline only; provide permissioned, de-identified inputs to run a study.")
