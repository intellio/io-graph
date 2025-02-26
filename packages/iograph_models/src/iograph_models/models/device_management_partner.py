from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementPartner(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	groupsRequiringPartnerEnrollment: list[DeviceManagementPartnerAssignment] = Field(alias="groupsRequiringPartnerEnrollment",)
	isConfigured: Optional[bool] = Field(default=None,alias="isConfigured",)
	lastHeartbeatDateTime: Optional[datetime] = Field(default=None,alias="lastHeartbeatDateTime",)
	partnerAppType: Optional[DeviceManagementPartnerAppType] = Field(default=None,alias="partnerAppType",)
	partnerState: Optional[DeviceManagementPartnerTenantState] = Field(default=None,alias="partnerState",)
	singleTenantAppId: Optional[str] = Field(default=None,alias="singleTenantAppId",)
	whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime: Optional[datetime] = Field(default=None,alias="whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime",)
	whenPartnerDevicesWillBeRemovedDateTime: Optional[datetime] = Field(default=None,alias="whenPartnerDevicesWillBeRemovedDateTime",)

from .device_management_partner_assignment import DeviceManagementPartnerAssignment
from .device_management_partner_app_type import DeviceManagementPartnerAppType
from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState

