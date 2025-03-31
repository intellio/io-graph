from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LogonUser(BaseModel):
	accountDomain: Optional[str] = Field(alias="accountDomain", default=None,)
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	accountType: Optional[UserAccountSecurityType | str] = Field(alias="accountType", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	logonId: Optional[str] = Field(alias="logonId", default=None,)
	logonTypes: Optional[list[LogonType | str]] = Field(alias="logonTypes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_account_security_type import UserAccountSecurityType
from .logon_type import LogonType
