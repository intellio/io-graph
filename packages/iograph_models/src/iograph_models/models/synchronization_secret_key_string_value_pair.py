from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationSecretKeyStringValuePair(BaseModel):
	key: Optional[SynchronizationSecret] = Field(default=None,alias="key",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_secret import SynchronizationSecret

