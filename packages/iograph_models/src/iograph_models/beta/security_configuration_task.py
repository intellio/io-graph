from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityConfigurationTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityConfigurationTask"] = Field(alias="@odata.type", default="#microsoft.graph.securityConfigurationTask")
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	category: Optional[DeviceAppManagementTaskCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creator: Optional[str] = Field(alias="creator", default=None,)
	creatorNotes: Optional[str] = Field(alias="creatorNotes", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime", default=None,)
	priority: Optional[DeviceAppManagementTaskPriority | str] = Field(alias="priority", default=None,)
	status: Optional[DeviceAppManagementTaskStatus | str] = Field(alias="status", default=None,)
	applicablePlatform: Optional[EndpointSecurityConfigurationApplicablePlatform | str] = Field(alias="applicablePlatform", default=None,)
	endpointSecurityPolicy: Optional[EndpointSecurityConfigurationType | str] = Field(alias="endpointSecurityPolicy", default=None,)
	endpointSecurityPolicyProfile: Optional[EndpointSecurityConfigurationProfileType | str] = Field(alias="endpointSecurityPolicyProfile", default=None,)
	insights: Optional[str] = Field(alias="insights", default=None,)
	intendedSettings: Optional[list[KeyValuePair]] = Field(alias="intendedSettings", default=None,)
	managedDeviceCount: Optional[int] = Field(alias="managedDeviceCount", default=None,)
	managedDevices: Optional[list[VulnerableManagedDevice]] = Field(alias="managedDevices", default=None,)

from .device_app_management_task_category import DeviceAppManagementTaskCategory
from .device_app_management_task_priority import DeviceAppManagementTaskPriority
from .device_app_management_task_status import DeviceAppManagementTaskStatus
from .endpoint_security_configuration_applicable_platform import EndpointSecurityConfigurationApplicablePlatform
from .endpoint_security_configuration_type import EndpointSecurityConfigurationType
from .endpoint_security_configuration_profile_type import EndpointSecurityConfigurationProfileType
from .key_value_pair import KeyValuePair
from .vulnerable_managed_device import VulnerableManagedDevice

