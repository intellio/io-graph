from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[ManagedAppConfiguration, TargetedManagedAppConfiguration, ManagedAppProtection, DefaultManagedAppProtection, TargetedManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, WindowsInformationProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy, WindowsManagedAppProtection],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

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
from .windows_managed_app_protection import WindowsManagedAppProtection

