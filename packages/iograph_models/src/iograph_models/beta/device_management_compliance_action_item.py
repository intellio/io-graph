from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementComplianceActionItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actionType: Optional[DeviceManagementComplianceActionType | str] = Field(alias="actionType", default=None,)
	gracePeriodHours: Optional[int] = Field(alias="gracePeriodHours", default=None,)
	notificationMessageCCList: Optional[list[str]] = Field(alias="notificationMessageCCList", default=None,)
	notificationTemplateId: Optional[str] = Field(alias="notificationTemplateId", default=None,)

from .device_management_compliance_action_type import DeviceManagementComplianceActionType

