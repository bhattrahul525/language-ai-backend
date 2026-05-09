"""API routers package."""

from typing import Any


class RouterHandler:
    """Template for router handler units."""

    def handle(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Override with endpoint-specific business mapping."""
        return payload
