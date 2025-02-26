from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MdmWindowsInformationProtectionPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[str] = Field(default=None,alias="version",)
	azureRightsManagementServicesAllowed: Optional[bool] = Field(default=None,alias="azureRightsManagementServicesAllowed",)
	dataRecoveryCertificate: Optional[WindowsInformationProtectionDataRecoveryCertificate] = Field(default=None,alias="dataRecoveryCertificate",)
	enforcementLevel: Optional[WindowsInformationProtectionEnforcementLevel] = Field(default=None,alias="enforcementLevel",)
	enterpriseDomain: Optional[str] = Field(default=None,alias="enterpriseDomain",)
	enterpriseInternalProxyServers: list[WindowsInformationProtectionResourceCollection] = Field(alias="enterpriseInternalProxyServers",)
	enterpriseIPRanges: list[WindowsInformationProtectionIPRangeCollection] = Field(alias="enterpriseIPRanges",)
	enterpriseIPRangesAreAuthoritative: Optional[bool] = Field(default=None,alias="enterpriseIPRangesAreAuthoritative",)
	enterpriseNetworkDomainNames: list[WindowsInformationProtectionResourceCollection] = Field(alias="enterpriseNetworkDomainNames",)
	enterpriseProtectedDomainNames: list[WindowsInformationProtectionResourceCollection] = Field(alias="enterpriseProtectedDomainNames",)
	enterpriseProxiedDomains: list[WindowsInformationProtectionProxiedDomainCollection] = Field(alias="enterpriseProxiedDomains",)
	enterpriseProxyServers: list[WindowsInformationProtectionResourceCollection] = Field(alias="enterpriseProxyServers",)
	enterpriseProxyServersAreAuthoritative: Optional[bool] = Field(default=None,alias="enterpriseProxyServersAreAuthoritative",)
	exemptApps: list[WindowsInformationProtectionApp] = Field(alias="exemptApps",)
	iconsVisible: Optional[bool] = Field(default=None,alias="iconsVisible",)
	indexingEncryptedStoresOrItemsBlocked: Optional[bool] = Field(default=None,alias="indexingEncryptedStoresOrItemsBlocked",)
	isAssigned: Optional[bool] = Field(default=None,alias="isAssigned",)
	neutralDomainResources: list[WindowsInformationProtectionResourceCollection] = Field(alias="neutralDomainResources",)
	protectedApps: list[WindowsInformationProtectionApp] = Field(alias="protectedApps",)
	protectionUnderLockConfigRequired: Optional[bool] = Field(default=None,alias="protectionUnderLockConfigRequired",)
	revokeOnUnenrollDisabled: Optional[bool] = Field(default=None,alias="revokeOnUnenrollDisabled",)
	rightsManagementServicesTemplateId: Optional[UUID] = Field(default=None,alias="rightsManagementServicesTemplateId",)
	smbAutoEncryptedFileExtensions: list[WindowsInformationProtectionResourceCollection] = Field(alias="smbAutoEncryptedFileExtensions",)
	assignments: list[TargetedManagedAppPolicyAssignment] = Field(alias="assignments",)
	exemptAppLockerFiles: list[WindowsInformationProtectionAppLockerFile] = Field(alias="exemptAppLockerFiles",)
	protectedAppLockerFiles: list[WindowsInformationProtectionAppLockerFile] = Field(alias="protectedAppLockerFiles",)

from .windows_information_protection_data_recovery_certificate import WindowsInformationProtectionDataRecoveryCertificate
from .windows_information_protection_enforcement_level import WindowsInformationProtectionEnforcementLevel
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_i_p_range_collection import WindowsInformationProtectionIPRangeCollection
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_app import WindowsInformationProtectionApp
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_app import WindowsInformationProtectionApp
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile

