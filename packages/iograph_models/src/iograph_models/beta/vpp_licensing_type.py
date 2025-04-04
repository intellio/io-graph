from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VppLicensingType(BaseModel):
	supportDeviceLicensing: Optional[bool] = Field(alias="supportDeviceLicensing", default=None,)
	supportsDeviceLicensing: Optional[bool] = Field(alias="supportsDeviceLicensing", default=None,)
	supportsUserLicensing: Optional[bool] = Field(alias="supportsUserLicensing", default=None,)
	supportUserLicensing: Optional[bool] = Field(alias="supportUserLicensing", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

