from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Year_fracPostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	basis: Optional[str] = Field(default=None,alias="basis",)


