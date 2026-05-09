"""Business services package."""

from typing import Any


class ServiceBase:
    """Base class for service-layer orchestration."""

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        """Override with domain-specific service logic."""
        return data
