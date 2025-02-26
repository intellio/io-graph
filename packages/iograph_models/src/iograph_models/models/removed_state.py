from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RemovedState(BaseModel):
	reason: Optional[str] = Field(default=None,alias="reason",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


