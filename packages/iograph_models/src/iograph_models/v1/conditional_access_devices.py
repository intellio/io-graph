from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessDevices(BaseModel):
	deviceFilter: Optional[ConditionalAccessFilter] = Field(alias="deviceFilter", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_filter import ConditionalAccessFilter
