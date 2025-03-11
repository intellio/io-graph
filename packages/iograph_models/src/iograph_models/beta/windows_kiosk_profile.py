from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskProfile(BaseModel):
	appConfiguration: SerializeAsAny[Optional[WindowsKioskAppConfiguration]] = Field(alias="appConfiguration",default=None,)
	profileId: Optional[str] = Field(alias="profileId",default=None,)
	profileName: Optional[str] = Field(alias="profileName",default=None,)
	userAccountsConfiguration: SerializeAsAny[Optional[list[WindowsKioskUser]]] = Field(alias="userAccountsConfiguration",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
from .windows_kiosk_user import WindowsKioskUser

