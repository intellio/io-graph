from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContentTypeInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ContentTypeInfo]] = Field(alias="value", default=None,)

from .content_type_info import ContentTypeInfo
