from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserAppInstallStatus(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount",default=None,)
	installedDeviceCount: Optional[int] = Field(alias="installedDeviceCount",default=None,)
	notInstalledDeviceCount: Optional[int] = Field(alias="notInstalledDeviceCount",default=None,)
	userName: Optional[str] = Field(alias="userName",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	app: SerializeAsAny[Optional[MobileApp]] = Field(alias="app",default=None,)
	deviceStatuses: Optional[list[MobileAppInstallStatus]] = Field(alias="deviceStatuses",default=None,)

from .mobile_app import MobileApp
from .mobile_app_install_status import MobileAppInstallStatus

