from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LicenseProcessingState(BaseModel):
	state: Optional[str] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


