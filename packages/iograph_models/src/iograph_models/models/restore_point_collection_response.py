from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestorePointCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RestorePoint] = Field(alias="value",)

from .restore_point import RestorePoint

