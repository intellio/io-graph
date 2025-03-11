from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppIntentAndState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	managedDeviceIdentifier: Optional[str] = Field(alias="managedDeviceIdentifier",default=None,)
	mobileAppList: Optional[list[MobileAppIntentAndStateDetail]] = Field(alias="mobileAppList",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)

from .mobile_app_intent_and_state_detail import MobileAppIntentAndStateDetail

