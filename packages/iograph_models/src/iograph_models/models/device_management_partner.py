from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementPartner(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	groupsRequiringPartnerEnrollment: Optional[list[DeviceManagementPartnerAssignment]] = Field(alias="groupsRequiringPartnerEnrollment",default=None,)
	isConfigured: Optional[bool] = Field(alias="isConfigured",default=None,)
	lastHeartbeatDateTime: Optional[datetime] = Field(alias="lastHeartbeatDateTime",default=None,)
	partnerAppType: Optional[str | DeviceManagementPartnerAppType] = Field(alias="partnerAppType",default=None,)
	partnerState: Optional[str | DeviceManagementPartnerTenantState] = Field(alias="partnerState",default=None,)
	singleTenantAppId: Optional[str] = Field(alias="singleTenantAppId",default=None,)
	whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime: Optional[datetime] = Field(alias="whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime",default=None,)
	whenPartnerDevicesWillBeRemovedDateTime: Optional[datetime] = Field(alias="whenPartnerDevicesWillBeRemovedDateTime",default=None,)

from .device_management_partner_assignment import DeviceManagementPartnerAssignment
from .device_management_partner_app_type import DeviceManagementPartnerAppType
from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState

