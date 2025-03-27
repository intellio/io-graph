from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceScopeActionResult(BaseModel):
	deviceScopeAction: Optional[DeviceScopeAction] = Field(alias="deviceScopeAction", default=None,)
	deviceScopeId: Optional[str] = Field(alias="deviceScopeId", default=None,)
	failedMessage: Optional[str] = Field(alias="failedMessage", default=None,)
	status: Optional[DeviceScopeActionStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_scope_action import DeviceScopeAction
from .device_scope_action_status import DeviceScopeActionStatus

