from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAppManagementTaskCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AppVulnerabilityTask, SecurityConfigurationTask, UnmanagedDeviceDiscoveryTask],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .app_vulnerability_task import AppVulnerabilityTask
from .security_configuration_task import SecurityConfigurationTask
from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask

