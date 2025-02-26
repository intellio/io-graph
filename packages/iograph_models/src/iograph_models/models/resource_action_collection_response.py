from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResourceActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ResourceAction] = Field(alias="value",)

from .resource_action import ResourceAction

