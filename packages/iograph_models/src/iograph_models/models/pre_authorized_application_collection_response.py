from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PreAuthorizedApplicationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PreAuthorizedApplication] = Field(alias="value",)

from .pre_authorized_application import PreAuthorizedApplication

