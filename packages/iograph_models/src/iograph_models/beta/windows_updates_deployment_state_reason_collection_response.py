from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDeploymentStateReasonCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsUpdatesDeploymentStateReason]] = Field(alias="value",default=None,)

from .windows_updates_deployment_state_reason import WindowsUpdatesDeploymentStateReason

