from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserSecurityState(BaseModel):
	aadUserId: Optional[str] = Field(alias="aadUserId", default=None,)
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	emailRole: Optional[EmailRole | str] = Field(alias="emailRole", default=None,)
	isVpn: Optional[bool] = Field(alias="isVpn", default=None,)
	logonDateTime: Optional[datetime] = Field(alias="logonDateTime", default=None,)
	logonId: Optional[str] = Field(alias="logonId", default=None,)
	logonIp: Optional[str] = Field(alias="logonIp", default=None,)
	logonLocation: Optional[str] = Field(alias="logonLocation", default=None,)
	logonType: Optional[LogonType | str] = Field(alias="logonType", default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	userAccountType: Optional[UserAccountSecurityType | str] = Field(alias="userAccountType", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .email_role import EmailRole
from .logon_type import LogonType
from .user_account_security_type import UserAccountSecurityType
