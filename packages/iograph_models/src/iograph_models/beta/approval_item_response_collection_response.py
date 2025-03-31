from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApprovalItemResponseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ApprovalItemResponse]] = Field(alias="value", default=None,)

from .approval_item_response import ApprovalItemResponse
