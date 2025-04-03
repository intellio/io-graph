from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class RemoteActionAudit(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.remoteActionAudit"] = Field(alias="@odata.type", default="#microsoft.graph.remoteActionAudit")
	action: Optional[RemoteAction | str] = Field(alias="action", default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState", default=None,)
	bulkDeviceActionId: Optional[str] = Field(alias="bulkDeviceActionId", default=None,)
	deviceActionCategory: Optional[DeviceActionCategory | str] = Field(alias="deviceActionCategory", default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceIMEI: Optional[str] = Field(alias="deviceIMEI", default=None,)
	deviceOwnerUserPrincipalName: Optional[str] = Field(alias="deviceOwnerUserPrincipalName", default=None,)
	initiatedByUserPrincipalName: Optional[str] = Field(alias="initiatedByUserPrincipalName", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	requestDateTime: Optional[datetime] = Field(alias="requestDateTime", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

from .remote_action import RemoteAction
from .action_state import ActionState
from .device_action_category import DeviceActionCategory
