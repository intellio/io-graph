from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceActionItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actionType: Optional[DeviceComplianceActionType] = Field(default=None,alias="actionType",)
	gracePeriodHours: Optional[int] = Field(default=None,alias="gracePeriodHours",)
	notificationMessageCCList: Optional[list[str]] = Field(default=None,alias="notificationMessageCCList",)
	notificationTemplateId: Optional[str] = Field(default=None,alias="notificationTemplateId",)

from .device_compliance_action_type import DeviceComplianceActionType

