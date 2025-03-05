from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VdbPostRequest(BaseModel):
	cost: Optional[str] = Field(default=None,alias="cost",)
	salvage: Optional[str] = Field(default=None,alias="salvage",)
	life: Optional[str] = Field(default=None,alias="life",)
	startPeriod: Optional[str] = Field(default=None,alias="startPeriod",)
	endPeriod: Optional[str] = Field(default=None,alias="endPeriod",)
	factor: Optional[str] = Field(default=None,alias="factor",)
	noSwitch: Optional[str] = Field(default=None,alias="noSwitch",)


