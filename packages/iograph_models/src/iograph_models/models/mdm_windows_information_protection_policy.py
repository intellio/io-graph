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
	enterpriseInternalProxyServers: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(default=None,alias="enterpriseInternalProxyServers",)
	enterpriseIPRanges: Optional[list[WindowsInformationProtectionIPRangeCollection]] = Field(default=None,alias="enterpriseIPRanges",)
	enterpriseIPRangesAreAuthoritative: Optional[bool] = Field(default=None,alias="enterpriseIPRangesAreAuthoritative",)
	enterpriseNetworkDomainNames: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(default=None,alias="enterpriseNetworkDomainNames",)
	enterpriseProtectedDomainNames: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(default=None,alias="enterpriseProtectedDomainNames",)
	enterpriseProxiedDomains: Optional[list[WindowsInformationProtectionProxiedDomainCollection]] = Field(default=None,alias="enterpriseProxiedDomains",)
	enterpriseProxyServers: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(default=None,alias="enterpriseProxyServers",)
	enterpriseProxyServersAreAuthoritative: Optional[bool] = Field(default=None,alias="enterpriseProxyServersAreAuthoritative",)
	exemptApps: Optional[list[WindowsInformationProtectionApp]] = Field(default=None,alias="exemptApps",)
	iconsVisible: Optional[bool] = Field(default=None,alias="iconsVisible",)
	indexingEncryptedStoresOrItemsBlocked: Optional[bool] = Field(default=None,alias="indexingEncryptedStoresOrItemsBlocked",)
	isAssigned: Optional[bool] = Field(default=None,alias="isAssigned",)
	neutralDomainResources: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(default=None,alias="neutralDomainResources",)
	protectedApps: Optional[list[WindowsInformationProtectionApp]] = Field(default=None,alias="protectedApps",)
	protectionUnderLockConfigRequired: Optional[bool] = Field(default=None,alias="protectionUnderLockConfigRequired",)
	revokeOnUnenrollDisabled: Optional[bool] = Field(default=None,alias="revokeOnUnenrollDisabled",)
	rightsManagementServicesTemplateId: Optional[UUID] = Field(default=None,alias="rightsManagementServicesTemplateId",)
	smbAutoEncryptedFileExtensions: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(default=None,alias="smbAutoEncryptedFileExtensions",)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(default=None,alias="assignments",)
	exemptAppLockerFiles: Optional[list[WindowsInformationProtectionAppLockerFile]] = Field(default=None,alias="exemptAppLockerFiles",)
	protectedAppLockerFiles: Optional[list[WindowsInformationProtectionAppLockerFile]] = Field(default=None,alias="protectedAppLockerFiles",)

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

