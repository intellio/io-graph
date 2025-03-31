from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidDeviceOwnerEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerEnrollmentProfile"] = Field(alias="@odata.type",)
	accountId: Optional[str] = Field(alias="accountId", default=None,)
	configureWifi: Optional[bool] = Field(alias="configureWifi", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enrolledDeviceCount: Optional[int] = Field(alias="enrolledDeviceCount", default=None,)
	enrollmentMode: Optional[AndroidDeviceOwnerEnrollmentMode | str] = Field(alias="enrollmentMode", default=None,)
	enrollmentTokenType: Optional[AndroidDeviceOwnerEnrollmentTokenType | str] = Field(alias="enrollmentTokenType", default=None,)
	enrollmentTokenUsageCount: Optional[int] = Field(alias="enrollmentTokenUsageCount", default=None,)
	isTeamsDeviceProfile: Optional[bool] = Field(alias="isTeamsDeviceProfile", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	qrCodeContent: Optional[str] = Field(alias="qrCodeContent", default=None,)
	qrCodeImage: Optional[MimeContent] = Field(alias="qrCodeImage", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	tokenCreationDateTime: Optional[datetime] = Field(alias="tokenCreationDateTime", default=None,)
	tokenExpirationDateTime: Optional[datetime] = Field(alias="tokenExpirationDateTime", default=None,)
	tokenValue: Optional[str] = Field(alias="tokenValue", default=None,)
	wifiHidden: Optional[bool] = Field(alias="wifiHidden", default=None,)
	wifiPassword: Optional[str] = Field(alias="wifiPassword", default=None,)
	wifiSecurityType: Optional[AospWifiSecurityType | str] = Field(alias="wifiSecurityType", default=None,)
	wifiSsid: Optional[str] = Field(alias="wifiSsid", default=None,)

from .android_device_owner_enrollment_mode import AndroidDeviceOwnerEnrollmentMode
from .android_device_owner_enrollment_token_type import AndroidDeviceOwnerEnrollmentTokenType
from .mime_content import MimeContent
from .aosp_wifi_security_type import AospWifiSecurityType
