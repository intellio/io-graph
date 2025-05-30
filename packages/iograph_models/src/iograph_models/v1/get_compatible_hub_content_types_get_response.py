from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_compatible_hub_content_typesGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ContentType]] = Field(alias="value", default=None,)

from .content_type import ContentType
