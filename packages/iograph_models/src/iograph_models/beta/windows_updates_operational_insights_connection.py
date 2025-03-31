from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsUpdatesOperationalInsightsConnection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.operationalInsightsConnection"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.operationalInsightsConnection")
	state: Optional[WindowsUpdatesResourceConnectionState | str] = Field(alias="state", default=None,)
	azureResourceGroupName: Optional[str] = Field(alias="azureResourceGroupName", default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId", default=None,)
	workspaceName: Optional[str] = Field(alias="workspaceName", default=None,)

from .windows_updates_resource_connection_state import WindowsUpdatesResourceConnectionState
