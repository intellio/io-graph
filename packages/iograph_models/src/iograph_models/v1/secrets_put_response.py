from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecretsPutResponse(BaseModel):
	value: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(alias="value", default=None,)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
