from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsInformationProtectionPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.windowsInformationProtectionPolicy")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	azureRightsManagementServicesAllowed: Optional[bool] = Field(alias="azureRightsManagementServicesAllowed", default=None,)
	dataRecoveryCertificate: Optional[WindowsInformationProtectionDataRecoveryCertificate] = Field(alias="dataRecoveryCertificate", default=None,)
	enforcementLevel: Optional[WindowsInformationProtectionEnforcementLevel | str] = Field(alias="enforcementLevel", default=None,)
	enterpriseDomain: Optional[str] = Field(alias="enterpriseDomain", default=None,)
	enterpriseInternalProxyServers: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseInternalProxyServers", default=None,)
	enterpriseIPRanges: Optional[list[WindowsInformationProtectionIPRangeCollection]] = Field(alias="enterpriseIPRanges", default=None,)
	enterpriseIPRangesAreAuthoritative: Optional[bool] = Field(alias="enterpriseIPRangesAreAuthoritative", default=None,)
	enterpriseNetworkDomainNames: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseNetworkDomainNames", default=None,)
	enterpriseProtectedDomainNames: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseProtectedDomainNames", default=None,)
	enterpriseProxiedDomains: Optional[list[WindowsInformationProtectionProxiedDomainCollection]] = Field(alias="enterpriseProxiedDomains", default=None,)
	enterpriseProxyServers: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="enterpriseProxyServers", default=None,)
	enterpriseProxyServersAreAuthoritative: Optional[bool] = Field(alias="enterpriseProxyServersAreAuthoritative", default=None,)
	exemptApps: Optional[list[Annotated[Union[WindowsInformationProtectionDesktopApp, WindowsInformationProtectionStoreApp]],Field(discriminator="odata_type")]]] = Field(alias="exemptApps", default=None,)
	iconsVisible: Optional[bool] = Field(alias="iconsVisible", default=None,)
	indexingEncryptedStoresOrItemsBlocked: Optional[bool] = Field(alias="indexingEncryptedStoresOrItemsBlocked", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	neutralDomainResources: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="neutralDomainResources", default=None,)
	protectedApps: Optional[list[Annotated[Union[WindowsInformationProtectionDesktopApp, WindowsInformationProtectionStoreApp]],Field(discriminator="odata_type")]]] = Field(alias="protectedApps", default=None,)
	protectionUnderLockConfigRequired: Optional[bool] = Field(alias="protectionUnderLockConfigRequired", default=None,)
	revokeOnUnenrollDisabled: Optional[bool] = Field(alias="revokeOnUnenrollDisabled", default=None,)
	rightsManagementServicesTemplateId: Optional[UUID] = Field(alias="rightsManagementServicesTemplateId", default=None,)
	smbAutoEncryptedFileExtensions: Optional[list[WindowsInformationProtectionResourceCollection]] = Field(alias="smbAutoEncryptedFileExtensions", default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments", default=None,)
	exemptAppLockerFiles: Optional[list[WindowsInformationProtectionAppLockerFile]] = Field(alias="exemptAppLockerFiles", default=None,)
	protectedAppLockerFiles: Optional[list[WindowsInformationProtectionAppLockerFile]] = Field(alias="protectedAppLockerFiles", default=None,)
	daysWithoutContactBeforeUnenroll: Optional[int] = Field(alias="daysWithoutContactBeforeUnenroll", default=None,)
	mdmEnrollmentUrl: Optional[str] = Field(alias="mdmEnrollmentUrl", default=None,)
	minutesOfInactivityBeforeDeviceLock: Optional[int] = Field(alias="minutesOfInactivityBeforeDeviceLock", default=None,)
	numberOfPastPinsRemembered: Optional[int] = Field(alias="numberOfPastPinsRemembered", default=None,)
	passwordMaximumAttemptCount: Optional[int] = Field(alias="passwordMaximumAttemptCount", default=None,)
	pinExpirationDays: Optional[int] = Field(alias="pinExpirationDays", default=None,)
	pinLowercaseLetters: Optional[WindowsInformationProtectionPinCharacterRequirements | str] = Field(alias="pinLowercaseLetters", default=None,)
	pinMinimumLength: Optional[int] = Field(alias="pinMinimumLength", default=None,)
	pinSpecialCharacters: Optional[WindowsInformationProtectionPinCharacterRequirements | str] = Field(alias="pinSpecialCharacters", default=None,)
	pinUppercaseLetters: Optional[WindowsInformationProtectionPinCharacterRequirements | str] = Field(alias="pinUppercaseLetters", default=None,)
	revokeOnMdmHandoffDisabled: Optional[bool] = Field(alias="revokeOnMdmHandoffDisabled", default=None,)
	windowsHelloForBusinessBlocked: Optional[bool] = Field(alias="windowsHelloForBusinessBlocked", default=None,)

from .windows_information_protection_data_recovery_certificate import WindowsInformationProtectionDataRecoveryCertificate
from .windows_information_protection_enforcement_level import WindowsInformationProtectionEnforcementLevel
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_i_p_range_collection import WindowsInformationProtectionIPRangeCollection
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp
from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
from .windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements
from .windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements
from .windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements

