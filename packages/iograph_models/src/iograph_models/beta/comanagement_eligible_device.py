from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ComanagementEligibleDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.comanagementEligibleDevice"] = Field(alias="@odata.type", default="#microsoft.graph.comanagementEligibleDevice")
	clientRegistrationStatus: Optional[DeviceRegistrationState | str] = Field(alias="clientRegistrationStatus", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceType: Optional[DeviceType | str] = Field(alias="deviceType", default=None,)
	entitySource: Optional[int] = Field(alias="entitySource", default=None,)
	managementAgents: Optional[ManagementAgentType | str] = Field(alias="managementAgents", default=None,)
	managementState: Optional[ManagementState | str] = Field(alias="managementState", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	mdmStatus: Optional[str] = Field(alias="mdmStatus", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	osDescription: Optional[str] = Field(alias="osDescription", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	ownerType: Optional[OwnerType | str] = Field(alias="ownerType", default=None,)
	referenceId: Optional[str] = Field(alias="referenceId", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	status: Optional[ComanagementEligibleType | str] = Field(alias="status", default=None,)
	upn: Optional[str] = Field(alias="upn", default=None,)
	userEmail: Optional[str] = Field(alias="userEmail", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

from .device_registration_state import DeviceRegistrationState
from .device_type import DeviceType
from .management_agent_type import ManagementAgentType
from .management_state import ManagementState
from .owner_type import OwnerType
from .comanagement_eligible_type import ComanagementEligibleType
