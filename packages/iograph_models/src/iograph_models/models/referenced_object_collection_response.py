from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReferencedObjectCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ReferencedObject] = Field(alias="value",)

from .referenced_object import ReferencedObject

