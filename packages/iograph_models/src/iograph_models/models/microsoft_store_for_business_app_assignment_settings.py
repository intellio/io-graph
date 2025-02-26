from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftStoreForBusinessAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	useDeviceContext: Optional[bool] = Field(default=None,alias="useDeviceContext",)


