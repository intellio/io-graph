from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RetireScheduledManagedDevice(BaseModel):
	complianceState: Optional[ComplianceStatus | str] = Field(alias="complianceState", default=None,)
	deviceCompliancePolicyId: Optional[str] = Field(alias="deviceCompliancePolicyId", default=None,)
	deviceCompliancePolicyName: Optional[str] = Field(alias="deviceCompliancePolicyName", default=None,)
	deviceType: Optional[DeviceType | str] = Field(alias="deviceType", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName", default=None,)
	managementAgent: Optional[ManagementAgentType | str] = Field(alias="managementAgent", default=None,)
	ownerType: Optional[ManagedDeviceOwnerType | str] = Field(alias="ownerType", default=None,)
	retireAfterDateTime: Optional[datetime] = Field(alias="retireAfterDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .compliance_status import ComplianceStatus
from .device_type import DeviceType
from .management_agent_type import ManagementAgentType
from .managed_device_owner_type import ManagedDeviceOwnerType

