from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDeploymentStateReason(BaseModel):
	value: Optional[WindowsUpdatesDeploymentStateReasonValue | str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_updates_deployment_state_reason_value import WindowsUpdatesDeploymentStateReasonValue

