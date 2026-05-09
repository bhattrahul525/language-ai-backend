"""Model adapters package."""

from typing import Any


class ModelAdapter:
    """Base adapter for model loading and prediction."""

    def predict(self, features: dict[str, Any]) -> dict[str, Any]:
        """Override with framework-specific inference implementation."""
        return features
