from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.iosVppAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.iosVppAppAssignmentSettings")
	useDeviceLicensing: Optional[bool] = Field(alias="useDeviceLicensing", default=None,)
	vpnConfigurationId: Optional[str] = Field(alias="vpnConfigurationId", default=None,)


