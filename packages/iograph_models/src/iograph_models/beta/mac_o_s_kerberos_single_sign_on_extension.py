from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MacOSKerberosSingleSignOnExtension(BaseModel):
	odata_type: Literal["#microsoft.graph.macOSKerberosSingleSignOnExtension"] = Field(alias="@odata.type", default="#microsoft.graph.macOSKerberosSingleSignOnExtension")
	activeDirectorySiteCode: Optional[str] = Field(alias="activeDirectorySiteCode", default=None,)
	blockActiveDirectorySiteAutoDiscovery: Optional[bool] = Field(alias="blockActiveDirectorySiteAutoDiscovery", default=None,)
	blockAutomaticLogin: Optional[bool] = Field(alias="blockAutomaticLogin", default=None,)
	cacheName: Optional[str] = Field(alias="cacheName", default=None,)
	credentialBundleIdAccessControlList: Optional[list[str]] = Field(alias="credentialBundleIdAccessControlList", default=None,)
	credentialsCacheMonitored: Optional[bool] = Field(alias="credentialsCacheMonitored", default=None,)
	domainRealms: Optional[list[str]] = Field(alias="domainRealms", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	isDefaultRealm: Optional[bool] = Field(alias="isDefaultRealm", default=None,)
	kerberosAppsInBundleIdACLIncluded: Optional[bool] = Field(alias="kerberosAppsInBundleIdACLIncluded", default=None,)
	managedAppsInBundleIdACLIncluded: Optional[bool] = Field(alias="managedAppsInBundleIdACLIncluded", default=None,)
	modeCredentialUsed: Optional[str] = Field(alias="modeCredentialUsed", default=None,)
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
	preferredKDCs: Optional[list[str]] = Field(alias="preferredKDCs", default=None,)
	realm: Optional[str] = Field(alias="realm", default=None,)
	requireUserPresence: Optional[bool] = Field(alias="requireUserPresence", default=None,)
	signInHelpText: Optional[str] = Field(alias="signInHelpText", default=None,)
	tlsForLDAPRequired: Optional[bool] = Field(alias="tlsForLDAPRequired", default=None,)
	usernameLabelCustom: Optional[str] = Field(alias="usernameLabelCustom", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	userSetupDelayed: Optional[bool] = Field(alias="userSetupDelayed", default=None,)

