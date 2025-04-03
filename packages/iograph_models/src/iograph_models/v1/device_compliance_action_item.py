from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceComplianceActionItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceComplianceActionItem"] = Field(alias="@odata.type", default="#microsoft.graph.deviceComplianceActionItem")
	actionType: Optional[DeviceComplianceActionType | str] = Field(alias="actionType", default=None,)
	gracePeriodHours: Optional[int] = Field(alias="gracePeriodHours", default=None,)
	notificationMessageCCList: Optional[list[str]] = Field(alias="notificationMessageCCList", default=None,)
	notificationTemplateId: Optional[str] = Field(alias="notificationTemplateId", default=None,)

from .device_compliance_action_type import DeviceComplianceActionType
