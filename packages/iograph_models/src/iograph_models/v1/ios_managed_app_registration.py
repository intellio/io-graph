from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosManagedAppRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosManagedAppRegistration"] = Field(alias="@odata.type", default="#microsoft.graph.iosManagedAppRegistration")
	appIdentifier: Optional[Union[AndroidMobileAppIdentifier, IosMobileAppIdentifier]] = Field(alias="appIdentifier", default=None,discriminator="odata_type", )
	applicationVersion: Optional[str] = Field(alias="applicationVersion", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceTag: Optional[str] = Field(alias="deviceTag", default=None,)
	deviceType: Optional[str] = Field(alias="deviceType", default=None,)
	flaggedReasons: Optional[list[ManagedAppFlaggedReason | str]] = Field(alias="flaggedReasons", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	managementSdkVersion: Optional[str] = Field(alias="managementSdkVersion", default=None,)
	platformVersion: Optional[str] = Field(alias="platformVersion", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	appliedPolicies: Optional[list[Annotated[Union[ManagedAppConfiguration, TargetedManagedAppConfiguration, ManagedAppProtection, DefaultManagedAppProtection, TargetedManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, WindowsInformationProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy],Field(discriminator="odata_type")]]] = Field(alias="appliedPolicies", default=None,)
	intendedPolicies: Optional[list[Annotated[Union[ManagedAppConfiguration, TargetedManagedAppConfiguration, ManagedAppProtection, DefaultManagedAppProtection, TargetedManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, WindowsInformationProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy],Field(discriminator="odata_type")]]] = Field(alias="intendedPolicies", default=None,)
	operations: Optional[list[ManagedAppOperation]] = Field(alias="operations", default=None,)

from .android_mobile_app_identifier import AndroidMobileAppIdentifier
from .ios_mobile_app_identifier import IosMobileAppIdentifier
from .managed_app_flagged_reason import ManagedAppFlaggedReason
from .managed_app_configuration import ManagedAppConfiguration
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .managed_app_protection import ManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .targeted_managed_app_protection import TargetedManagedAppProtection
from .android_managed_app_protection import AndroidManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .windows_information_protection import WindowsInformationProtection
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .managed_app_configuration import ManagedAppConfiguration
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .managed_app_protection import ManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .targeted_managed_app_protection import TargetedManagedAppProtection
from .android_managed_app_protection import AndroidManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .windows_information_protection import WindowsInformationProtection
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .managed_app_operation import ManagedAppOperation

