"""ML service package root."""


class AppModule:
    """Base app module template for shared setup hooks."""

    name = "base-module"

    def setup(self) -> None:
        """Override to run module-level initialization."""
        return None
