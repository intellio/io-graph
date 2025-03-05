from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUnifiedGroupSourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityUnifiedGroupSource]] = Field(alias="value",default=None,)

from .security_unified_group_source import SecurityUnifiedGroupSource

