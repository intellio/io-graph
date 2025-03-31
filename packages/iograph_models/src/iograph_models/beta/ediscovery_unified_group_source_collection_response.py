from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EdiscoveryUnifiedGroupSourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EdiscoveryUnifiedGroupSource]] = Field(alias="value", default=None,)

from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
