from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignmentFilterEvaluateRequest(BaseModel):
	orderBy: Optional[list[str]] = Field(alias="orderBy", default=None,)
	platform: Optional[DevicePlatformType | str] = Field(alias="platform", default=None,)
	rule: Optional[str] = Field(alias="rule", default=None,)
	search: Optional[str] = Field(alias="search", default=None,)
	skip: Optional[int] = Field(alias="skip", default=None,)
	top: Optional[int] = Field(alias="top", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_platform_type import DevicePlatformType
