from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Acquire_access_tokenPostRequest(BaseModel):
	credentials: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(alias="credentials", default=None,)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

