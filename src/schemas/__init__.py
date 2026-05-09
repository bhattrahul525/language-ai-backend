"""Shared API schemas."""

from pydantic import BaseModel


class BasePayload(BaseModel):
    """Base schema class to standardize payload extensions."""

    pass
