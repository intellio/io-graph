from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ModifiedPropertyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ModifiedProperty] = Field(alias="value",)

from .modified_property import ModifiedProperty

