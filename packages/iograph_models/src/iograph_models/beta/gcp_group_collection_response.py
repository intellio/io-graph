from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GcpGroupCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GcpGroup]] = Field(alias="value", default=None,)

from .gcp_group import GcpGroup
