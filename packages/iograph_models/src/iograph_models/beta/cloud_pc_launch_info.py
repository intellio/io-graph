from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcLaunchInfo(BaseModel):
	cloudPcId: Optional[str] = Field(alias="cloudPcId", default=None,)
	cloudPcLaunchUrl: Optional[str] = Field(alias="cloudPcLaunchUrl", default=None,)
	windows365SwitchCompatible: Optional[bool] = Field(alias="windows365SwitchCompatible", default=None,)
	windows365SwitchNotCompatibleReason: Optional[str] = Field(alias="windows365SwitchNotCompatibleReason", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

