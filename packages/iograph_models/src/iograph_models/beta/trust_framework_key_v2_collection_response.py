from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrustFrameworkKey_v2CollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[TrustFrameworkKey_v2]] = Field(alias="value",default=None,)

from .trust_framework_key_v2 import TrustFrameworkKey_v2

