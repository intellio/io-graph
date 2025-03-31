from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrustFrameworkKeySetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TrustFrameworkKeySet]] = Field(alias="value", default=None,)

from .trust_framework_key_set import TrustFrameworkKeySet
