from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Execute_actionPostRequest(BaseModel):
	actionName: Optional[ManagedDeviceRemoteAction | str] = Field(alias="actionName",default=None,)
	keepEnrollmentData: Optional[bool] = Field(alias="keepEnrollmentData",default=None,)
	keepUserData: Optional[bool] = Field(alias="keepUserData",default=None,)
	persistEsimDataPlan: Optional[bool] = Field(alias="persistEsimDataPlan",default=None,)
	deviceIds: Optional[list[str]] = Field(alias="deviceIds",default=None,)
	notificationTitle: Optional[str] = Field(alias="notificationTitle",default=None,)
	notificationBody: Optional[str] = Field(alias="notificationBody",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	carrierUrl: Optional[str] = Field(alias="carrierUrl",default=None,)
	deprovisionReason: Optional[str] = Field(alias="deprovisionReason",default=None,)
	organizationalUnitPath: Optional[str] = Field(alias="organizationalUnitPath",default=None,)

from .managed_device_remote_action import ManagedDeviceRemoteAction

