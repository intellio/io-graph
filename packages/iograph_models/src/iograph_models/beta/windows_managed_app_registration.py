from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsManagedAppRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsManagedAppRegistration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsManagedAppRegistration")
	appIdentifier: Optional[Union[AndroidMobileAppIdentifier, IosMobileAppIdentifier, MacAppIdentifier, WindowsAppIdentifier]] = Field(alias="appIdentifier", default=None,discriminator="odata_type", )
	applicationVersion: Optional[str] = Field(alias="applicationVersion", default=None,)
	azureADDeviceId: Optional[str] = Field(alias="azureADDeviceId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deviceManufacturer: Optional[str] = Field(alias="deviceManufacturer", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceTag: Optional[str] = Field(alias="deviceTag", default=None,)
	deviceType: Optional[str] = Field(alias="deviceType", default=None,)
	flaggedReasons: Optional[list[ManagedAppFlaggedReason | str]] = Field(alias="flaggedReasons", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managementSdkVersion: Optional[str] = Field(alias="managementSdkVersion", default=None,)
	platformVersion: Optional[str] = Field(alias="platformVersion", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	appliedPolicies: Optional[list[Annotated[Union[TargetedManagedAppConfiguration, DefaultManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy, WindowsManagedAppProtection],Field(discriminator="odata_type")]]] = Field(alias="appliedPolicies", default=None,)
	intendedPolicies: Optional[list[Annotated[Union[TargetedManagedAppConfiguration, DefaultManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy, WindowsManagedAppProtection],Field(discriminator="odata_type")]]] = Field(alias="intendedPolicies", default=None,)
	managedAppLogCollectionRequests: Optional[list[ManagedAppLogCollectionRequest]] = Field(alias="managedAppLogCollectionRequests", default=None,)
	operations: Optional[list[ManagedAppOperation]] = Field(alias="operations", default=None,)

from .android_mobile_app_identifier import AndroidMobileAppIdentifier
from .ios_mobile_app_identifier import IosMobileAppIdentifier
from .mac_app_identifier import MacAppIdentifier
from .windows_app_identifier import WindowsAppIdentifier
from .managed_app_flagged_reason import ManagedAppFlaggedReason
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .default_managed_app_protection import DefaultManagedAppProtection
from .android_managed_app_protection import AndroidManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .windows_managed_app_protection import WindowsManagedAppProtection
from .managed_app_log_collection_request import ManagedAppLogCollectionRequest
from .managed_app_operation import ManagedAppOperation
