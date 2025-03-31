from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VppLicensingType(BaseModel):
	supportsDeviceLicensing: Optional[bool] = Field(alias="supportsDeviceLicensing", default=None,)
	supportsUserLicensing: Optional[bool] = Field(alias="supportsUserLicensing", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

