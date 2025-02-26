from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContentTypeInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ContentTypeInfo] = Field(alias="value",)

from .content_type_info import ContentTypeInfo

