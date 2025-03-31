from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlertTrigger(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

