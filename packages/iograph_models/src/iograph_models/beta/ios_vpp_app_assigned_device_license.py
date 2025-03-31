from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IosVppAppAssignedDeviceLicense(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosVppAppAssignedDeviceLicense"] = Field(alias="@odata.type",)
	userEmailAddress: Optional[str] = Field(alias="userEmailAddress", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)

