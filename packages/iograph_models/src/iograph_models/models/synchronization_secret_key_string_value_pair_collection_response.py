from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationSecretKeyStringValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SynchronizationSecretKeyStringValuePair] = Field(alias="value",)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

