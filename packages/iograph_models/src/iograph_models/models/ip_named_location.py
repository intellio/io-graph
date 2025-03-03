from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IpNamedLocation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	ipRanges: Optional[list[IpRange]] = Field(default=None,alias="ipRanges",)
	isTrusted: Optional[bool] = Field(default=None,alias="isTrusted",)

from .ip_range import IpRange

