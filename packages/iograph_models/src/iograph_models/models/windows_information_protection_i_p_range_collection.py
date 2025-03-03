from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionIPRangeCollection(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	ranges: Optional[list[IpRange]] = Field(default=None,alias="ranges",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .ip_range import IpRange

