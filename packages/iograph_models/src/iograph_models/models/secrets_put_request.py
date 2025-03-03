from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecretsPutRequest(BaseModel):
	value: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(default=None,alias="value",)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

