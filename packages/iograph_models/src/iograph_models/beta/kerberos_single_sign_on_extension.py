from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class KerberosSingleSignOnExtension(BaseModel):
	odata_type: Literal["#microsoft.graph.kerberosSingleSignOnExtension"] = Field(alias="@odata.type", default="#microsoft.graph.kerberosSingleSignOnExtension")
	activeDirectorySiteCode: Optional[str] = Field(alias="activeDirectorySiteCode", default=None,)
	blockActiveDirectorySiteAutoDiscovery: Optional[bool] = Field(alias="blockActiveDirectorySiteAutoDiscovery", default=None,)
	blockAutomaticLogin: Optional[bool] = Field(alias="blockAutomaticLogin", default=None,)
	cacheName: Optional[str] = Field(alias="cacheName", default=None,)
	credentialBundleIdAccessControlList: Optional[list[str]] = Field(alias="credentialBundleIdAccessControlList", default=None,)
	domainRealms: Optional[list[str]] = Field(alias="domainRealms", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	isDefaultRealm: Optional[bool] = Field(alias="isDefaultRealm", default=None,)
	passwordBlockModification: Optional[bool] = Field(alias="passwordBlockModification", default=None,)
	passwordChangeUrl: Optional[str] = Field(alias="passwordChangeUrl", default=None,)
	passwordEnableLocalSync: Optional[bool] = Field(alias="passwordEnableLocalSync", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordExpirationNotificationDays: Optional[int] = Field(alias="passwordExpirationNotificationDays", default=None,)
	passwordMinimumAgeDays: Optional[int] = Field(alias="passwordMinimumAgeDays", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount", default=None,)
	passwordRequireActiveDirectoryComplexity: Optional[bool] = Field(alias="passwordRequireActiveDirectoryComplexity", default=None,)
	passwordRequirementsDescription: Optional[str] = Field(alias="passwordRequirementsDescription", default=None,)
	realm: Optional[str] = Field(alias="realm", default=None,)
	requireUserPresence: Optional[bool] = Field(alias="requireUserPresence", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

