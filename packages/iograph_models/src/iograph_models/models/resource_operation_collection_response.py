from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResourceOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ResourceOperation] = Field(alias="value",)

from .resource_operation import ResourceOperation

