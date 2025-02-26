from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosDeviceType(BaseModel):
	iPad: Optional[bool] = Field(default=None,alias="iPad",)
	iPhoneAndIPod: Optional[bool] = Field(default=None,alias="iPhoneAndIPod",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


