from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VdbPostRequest(BaseModel):
	cost: Optional[str] = Field(alias="cost",default=None,)
	salvage: Optional[str] = Field(alias="salvage",default=None,)
	life: Optional[str] = Field(alias="life",default=None,)
	startPeriod: Optional[str] = Field(alias="startPeriod",default=None,)
	endPeriod: Optional[str] = Field(alias="endPeriod",default=None,)
	factor: Optional[str] = Field(alias="factor",default=None,)
	noSwitch: Optional[str] = Field(alias="noSwitch",default=None,)


