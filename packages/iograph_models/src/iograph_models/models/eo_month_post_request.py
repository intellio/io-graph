from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Eo_monthPostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	months: Optional[str] = Field(default=None,alias="months",)


