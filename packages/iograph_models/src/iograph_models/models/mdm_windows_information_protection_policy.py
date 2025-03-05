from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MdmWindowsInformationProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	azureRightsManagementServicesAllowed: Optional[bool] = Field(alias="azureRightsManagementServicesAllowed",default=None,)
	dataRecoveryCertificate: Optional[WindowsInformationProtectionDataRecoveryCertificate] = Field(alias="dataRecoveryCertificate",default=None,)
	enforcementLevel: Optional[str | WindowsInformationProtectionEnforcementLevel] = Field(alias="enforcementLevel",default=None,)
	enterpriseDomain: Optional[str] = Field(alias="enterpriseDomain",default=None,)
	enterpriseInternalProxyServers: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseInternalProxyServers",default=None,)
	enterpriseIPRanges: Optional[list[WindowsInformationProtectionIPRangeCollection]] = Field(alias="enterpriseIPRanges",default=None,)
	enterpriseIPRangesAreAuthoritative: Optional[bool] = Field(alias="enterpriseIPRangesAreAuthoritative",default=None,)
	enterpriseNetworkDomainNames: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseNetworkDomainNames",default=None,)
	enterpriseProtectedDomainNames: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseProtectedDomainNames",default=None,)
	enterpriseProxiedDomains: Optional[list[WindowsInformationProtectionProxiedDomainCollection]] = Field(alias="enterpriseProxiedDomains",default=None,)
	enterpriseProxyServers: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseProxyServers",default=None,)
	enterpriseProxyServersAreAuthoritative: Optional[bool] = Field(alias="enterpriseProxyServersAreAuthoritative",default=None,)
	exemptApps: SerializeAsAny[Optional[list[WindowsInformationProtectionApp]]] = Field(alias="exemptApps",default=None,)
	iconsVisible: Optional[bool] = Field(alias="iconsVisible",default=None,)
	indexingEncryptedStoresOrItemsBlocked: Optional[bool] = Field(alias="indexingEncryptedStoresOrItemsBlocked",default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned",default=None,)
	neutralDomainResources: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="neutralDomainResources",default=None,)
	protectedApps: SerializeAsAny[Optional[list[WindowsInformationProtectionApp]]] = Field(alias="protectedApps",default=None,)
	protectionUnderLockConfigRequired: Optional[bool] = Field(alias="protectionUnderLockConfigRequired",default=None,)
	revokeOnUnenrollDisabled: Optional[bool] = Field(alias="revokeOnUnenrollDisabled",default=None,)
	rightsManagementServicesTemplateId: Optional[UUID] = Field(alias="rightsManagementServicesTemplateId",default=None,)
	smbAutoEncryptedFileExtensions: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="smbAutoEncryptedFileExtensions",default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments",default=None,)
	exemptAppLockerFiles: Optional[list[WindowsInformationProtectionAppLockerFile]] = Field(alias="exemptAppLockerFiles",default=None,)
	protectedAppLockerFiles: Optional[list[WindowsInformationProtectionAppLockerFile]] = Field(alias="protectedAppLockerFiles",default=None,)

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

