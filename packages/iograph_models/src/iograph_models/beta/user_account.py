from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserAccount(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	signinName: Optional[str] = Field(alias="signinName", default=None,)
	status: Optional[AccountStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .account_status import AccountStatus
