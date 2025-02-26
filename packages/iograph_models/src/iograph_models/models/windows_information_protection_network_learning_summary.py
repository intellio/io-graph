from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionNetworkLearningSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceCount: Optional[int] = Field(default=None,alias="deviceCount",)
	url: Optional[str] = Field(default=None,alias="url",)


