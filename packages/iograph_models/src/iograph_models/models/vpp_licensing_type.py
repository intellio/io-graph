from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VppLicensingType(BaseModel):
	supportsDeviceLicensing: Optional[bool] = Field(default=None,alias="supportsDeviceLicensing",)
	supportsUserLicensing: Optional[bool] = Field(default=None,alias="supportsUserLicensing",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


