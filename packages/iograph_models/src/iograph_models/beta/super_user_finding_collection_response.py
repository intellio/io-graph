from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SuperUserFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SuperUserFinding]] = Field(alias="value", default=None,)

from .super_user_finding import SuperUserFinding
