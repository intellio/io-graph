from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName",default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionDeliveryStatus: Optional[ConfigurationManagerActionDeliveryStatus | str] = Field(alias="actionDeliveryStatus",default=None,)
	errorCode: Optional[int] = Field(alias="errorCode",default=None,)

from .action_state import ActionState
from .configuration_manager_action_delivery_status import ConfigurationManagerActionDeliveryStatus

