from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedAppOperation] = Field(alias="value",)

from .managed_app_operation import ManagedAppOperation

