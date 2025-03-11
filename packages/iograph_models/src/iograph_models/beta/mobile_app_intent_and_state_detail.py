from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppIntentAndStateDetail(BaseModel):
	applicationId: Optional[str] = Field(alias="applicationId",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	displayVersion: Optional[str] = Field(alias="displayVersion",default=None,)
	installState: Optional[ResultantAppState | str] = Field(alias="installState",default=None,)
	mobileAppIntent: Optional[MobileAppIntent | str] = Field(alias="mobileAppIntent",default=None,)
	supportedDeviceTypes: Optional[list[MobileAppSupportedDeviceType]] = Field(alias="supportedDeviceTypes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .resultant_app_state import ResultantAppState
from .mobile_app_intent import MobileAppIntent
from .mobile_app_supported_device_type import MobileAppSupportedDeviceType

