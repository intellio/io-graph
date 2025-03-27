from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Year_fracPostRequest(BaseModel):
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	basis: Optional[str] = Field(alias="basis", default=None,)


