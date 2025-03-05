from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessDevices(BaseModel):
	deviceFilter: Optional[ConditionalAccessFilter] = Field(default=None,alias="deviceFilter",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_filter import ConditionalAccessFilter

