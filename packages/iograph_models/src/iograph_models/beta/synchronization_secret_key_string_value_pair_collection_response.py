from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationSecretKeyStringValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(alias="value", default=None,)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
