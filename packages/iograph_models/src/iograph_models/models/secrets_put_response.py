from __future__ import annotations
from pydantic import BaseModel, Field


class SecretsPutResponse(BaseModel):
	value: list[SynchronizationSecretKeyStringValuePair] = Field(alias="value",)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

