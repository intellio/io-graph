from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserSecurityState(BaseModel):
	aadUserId: Optional[str] = Field(default=None,alias="aadUserId",)
	accountName: Optional[str] = Field(default=None,alias="accountName",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	emailRole: Optional[EmailRole] = Field(default=None,alias="emailRole",)
	isVpn: Optional[bool] = Field(default=None,alias="isVpn",)
	logonDateTime: Optional[datetime] = Field(default=None,alias="logonDateTime",)
	logonId: Optional[str] = Field(default=None,alias="logonId",)
	logonIp: Optional[str] = Field(default=None,alias="logonIp",)
	logonLocation: Optional[str] = Field(default=None,alias="logonLocation",)
	logonType: Optional[LogonType] = Field(default=None,alias="logonType",)
	onPremisesSecurityIdentifier: Optional[str] = Field(default=None,alias="onPremisesSecurityIdentifier",)
	riskScore: Optional[str] = Field(default=None,alias="riskScore",)
	userAccountType: Optional[UserAccountSecurityType] = Field(default=None,alias="userAccountType",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .email_role import EmailRole
from .logon_type import LogonType
from .user_account_security_type import UserAccountSecurityType

