from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsManagementAppHealthSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	healthyDeviceCount: Optional[int] = Field(alias="healthyDeviceCount", default=None,)
	unhealthyDeviceCount: Optional[int] = Field(alias="unhealthyDeviceCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)


