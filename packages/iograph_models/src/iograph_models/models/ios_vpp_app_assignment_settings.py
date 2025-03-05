from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	useDeviceLicensing: Optional[bool] = Field(default=None,alias="useDeviceLicensing",)
	vpnConfigurationId: Optional[str] = Field(default=None,alias="vpnConfigurationId",)


