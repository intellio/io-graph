from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppInstallStatus(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	displayVersion: Optional[str] = Field(alias="displayVersion",default=None,)
	errorCode: Optional[int] = Field(alias="errorCode",default=None,)
	installState: Optional[ResultantAppState | str] = Field(alias="installState",default=None,)
	installStateDetail: Optional[ResultantAppStateDetail | str] = Field(alias="installStateDetail",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	mobileAppInstallStatusValue: Optional[ResultantAppState | str] = Field(alias="mobileAppInstallStatusValue",default=None,)
	osDescription: Optional[str] = Field(alias="osDescription",default=None,)
	osVersion: Optional[str] = Field(alias="osVersion",default=None,)
	userName: Optional[str] = Field(alias="userName",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	app: SerializeAsAny[Optional[MobileApp]] = Field(alias="app",default=None,)

from .resultant_app_state import ResultantAppState
from .resultant_app_state_detail import ResultantAppStateDetail
from .resultant_app_state import ResultantAppState
from .mobile_app import MobileApp

