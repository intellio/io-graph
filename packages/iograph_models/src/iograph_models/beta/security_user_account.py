from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityUserAccount(BaseModel):
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	azureAdUserId: Optional[str] = Field(alias="azureAdUserId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	userSid: Optional[str] = Field(alias="userSid", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

