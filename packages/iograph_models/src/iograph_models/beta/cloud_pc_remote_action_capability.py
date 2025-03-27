from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcRemoteActionCapability(BaseModel):
	actionCapability: Optional[ActionCapability | str] = Field(alias="actionCapability", default=None,)
	actionName: Optional[CloudPcRemoteActionName | str] = Field(alias="actionName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .action_capability import ActionCapability
from .cloud_pc_remote_action_name import CloudPcRemoteActionName

