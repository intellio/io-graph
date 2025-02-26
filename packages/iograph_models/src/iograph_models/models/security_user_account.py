from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityUserAccount(BaseModel):
	accountName: Optional[str] = Field(default=None,alias="accountName",)
	azureAdUserId: Optional[str] = Field(default=None,alias="azureAdUserId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	userSid: Optional[str] = Field(default=None,alias="userSid",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


