from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ListItemVersionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ListItemVersion] = Field(alias="value",)

from .list_item_version import ListItemVersion

