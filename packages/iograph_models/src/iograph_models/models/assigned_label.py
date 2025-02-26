from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignedLabel(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	labelId: Optional[str] = Field(default=None,alias="labelId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


