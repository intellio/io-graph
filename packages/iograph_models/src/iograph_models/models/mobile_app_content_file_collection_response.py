from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileAppContentFileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MobileAppContentFile] = Field(alias="value",)

from .mobile_app_content_file import MobileAppContentFile

