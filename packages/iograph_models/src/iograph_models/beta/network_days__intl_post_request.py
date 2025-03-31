from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Network_days__intlPostRequest(BaseModel):
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	weekend: Optional[str] = Field(alias="weekend", default=None,)
	holidays: Optional[str] = Field(alias="holidays", default=None,)

