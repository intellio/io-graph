from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PreAuthorizedApplicationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[PreAuthorizedApplication]] = Field(default=None,alias="value",)

from .pre_authorized_application import PreAuthorizedApplication

