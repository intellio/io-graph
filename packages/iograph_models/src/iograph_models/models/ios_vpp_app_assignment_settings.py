from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	useDeviceLicensing: Optional[bool] = Field(alias="useDeviceLicensing",default=None,)
	vpnConfigurationId: Optional[str] = Field(alias="vpnConfigurationId",default=None,)


