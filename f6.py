"""f6 reference helpers for the Svensk Army Knife.

A position is a point in the triangle (lam, delta, alpha, summing to 1)
plus a mass, which is perpendicular to the triangle.

Standard library only, on purpose: anyone should be able to read and port this.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

SQRT3_2 = math.sqrt(3) / 2
TOLERANCE = 1e-3


@dataclass(frozen=True)
class Position:
    lam: float    # Λ  solo entity
    delta: float  # Δ  chaos
    alpha: float  # Α  order
    mass: float = 0.0

    def __post_init__(self) -> None:
        for name, value in (("lam", self.lam), ("delta", self.delta), ("alpha", self.alpha)):
            if value < 0:
                raise ValueError(f"{name} must be >= 0, got {value}")
        if self.mass < 0:
            raise ValueError(f"mass must be >= 0, got {self.mass}")
        total = self.lam + self.delta + self.alpha
        if abs(total - 1.0) > TOLERANCE:
            raise ValueError(f"lam + delta + alpha must equal 1, got {total}")

    @classmethod
    def from_weights(cls, lam: float, delta: float, alpha: float, mass: float = 0.0) -> "Position":
        """Build a Position from any non-negative weights by normalising them."""
        total = lam + delta + alpha
        if total <= 0:
            raise ValueError("at least one weight must be positive")
        return cls(lam / total, delta / total, alpha / total, mass)

    def to_xy(self) -> tuple[float, float]:
        """Flat coordinates: Λ at (0, 0), Δ at (1, 0), Α at (0.5, √3/2)."""
        return (self.delta + 0.5 * self.alpha, SQRT3_2 * self.alpha)

    def pole(self) -> str:
        """The nearest vertex as a single letter: 'Λ', 'Δ' or 'Α' (ties go Λ, Δ, Α)."""
        best = max((self.lam, "Λ"), (self.delta, "Δ"), (self.alpha, "Α"), key=lambda p: p[0])
        return best[1]


def distance(a: Position, b: Position) -> float:
    """Distance between two positions in the triangle (ignores mass).

    Use this to measure how far apart two people place the same word.
    """
    (ax, ay), (bx, by) = a.to_xy(), b.to_xy()
    return math.hypot(ax - bx, ay - by)
