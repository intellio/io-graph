from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Office365ActiveUserDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.office365ActiveUserDetail"] = Field(alias="@odata.type", default="#microsoft.graph.office365ActiveUserDetail")
	assignedProducts: Optional[list[str]] = Field(alias="assignedProducts", default=None,)
	deletedDate: Optional[str] = Field(alias="deletedDate", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	exchangeLastActivityDate: Optional[str] = Field(alias="exchangeLastActivityDate", default=None,)
	exchangeLicenseAssignDate: Optional[str] = Field(alias="exchangeLicenseAssignDate", default=None,)
	hasExchangeLicense: Optional[bool] = Field(alias="hasExchangeLicense", default=None,)
	hasOneDriveLicense: Optional[bool] = Field(alias="hasOneDriveLicense", default=None,)
	hasSharePointLicense: Optional[bool] = Field(alias="hasSharePointLicense", default=None,)
	hasSkypeForBusinessLicense: Optional[bool] = Field(alias="hasSkypeForBusinessLicense", default=None,)
	hasTeamsLicense: Optional[bool] = Field(alias="hasTeamsLicense", default=None,)
	hasYammerLicense: Optional[bool] = Field(alias="hasYammerLicense", default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted", default=None,)
	oneDriveLastActivityDate: Optional[str] = Field(alias="oneDriveLastActivityDate", default=None,)
	oneDriveLicenseAssignDate: Optional[str] = Field(alias="oneDriveLicenseAssignDate", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	sharePointLastActivityDate: Optional[str] = Field(alias="sharePointLastActivityDate", default=None,)
	sharePointLicenseAssignDate: Optional[str] = Field(alias="sharePointLicenseAssignDate", default=None,)
	skypeForBusinessLastActivityDate: Optional[str] = Field(alias="skypeForBusinessLastActivityDate", default=None,)
	skypeForBusinessLicenseAssignDate: Optional[str] = Field(alias="skypeForBusinessLicenseAssignDate", default=None,)
	teamsLastActivityDate: Optional[str] = Field(alias="teamsLastActivityDate", default=None,)
	teamsLicenseAssignDate: Optional[str] = Field(alias="teamsLicenseAssignDate", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	yammerLastActivityDate: Optional[str] = Field(alias="yammerLastActivityDate", default=None,)
	yammerLicenseAssignDate: Optional[str] = Field(alias="yammerLicenseAssignDate", default=None,)

