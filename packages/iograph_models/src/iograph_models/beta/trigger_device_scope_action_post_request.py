from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Trigger_device_scope_actionPostRequest(BaseModel):
	actionName: Optional[DeviceScopeAction] = Field(alias="actionName",default=None,)
	deviceScopeId: Optional[str] = Field(alias="deviceScopeId",default=None,)

from .device_scope_action import DeviceScopeAction

