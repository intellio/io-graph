from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserSecurityProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userSecurityProfile"] = Field(alias="@odata.type", default="#microsoft.graph.userSecurityProfile")
	accounts: Optional[list[UserAccount]] = Field(alias="accounts", default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId", default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation", default=None,)

from .user_account import UserAccount
from .security_vendor_information import SecurityVendorInformation
