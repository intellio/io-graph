from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Network_daysPostRequest(BaseModel):
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	holidays: Optional[str] = Field(alias="holidays", default=None,)


