from __future__ import annotations
from pydantic import BaseModel, Field


class Acquire_access_tokenPostRequest(BaseModel):
	credentials: list[SynchronizationSecretKeyStringValuePair] = Field(alias="credentials",)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

