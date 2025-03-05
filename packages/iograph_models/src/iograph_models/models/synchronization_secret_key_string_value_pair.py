from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationSecretKeyStringValuePair(BaseModel):
	key: Optional[str | SynchronizationSecret] = Field(alias="key",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_secret import SynchronizationSecret

