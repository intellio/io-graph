from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementPartner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementPartner"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementPartner")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	groupsRequiringPartnerEnrollment: Optional[list[DeviceManagementPartnerAssignment]] = Field(alias="groupsRequiringPartnerEnrollment", default=None,)
	isConfigured: Optional[bool] = Field(alias="isConfigured", default=None,)
	lastHeartbeatDateTime: Optional[datetime] = Field(alias="lastHeartbeatDateTime", default=None,)
	partnerAppType: Optional[DeviceManagementPartnerAppType | str] = Field(alias="partnerAppType", default=None,)
	partnerState: Optional[DeviceManagementPartnerTenantState | str] = Field(alias="partnerState", default=None,)
	singleTenantAppId: Optional[str] = Field(alias="singleTenantAppId", default=None,)
	whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime: Optional[datetime] = Field(alias="whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime", default=None,)
	whenPartnerDevicesWillBeRemovedDateTime: Optional[datetime] = Field(alias="whenPartnerDevicesWillBeRemovedDateTime", default=None,)

from .device_management_partner_assignment import DeviceManagementPartnerAssignment
from .device_management_partner_app_type import DeviceManagementPartnerAppType
from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState
