from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesOperationalInsightsConnection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	state: Optional[WindowsUpdatesResourceConnectionState | str] = Field(alias="state",default=None,)
	azureResourceGroupName: Optional[str] = Field(alias="azureResourceGroupName",default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId",default=None,)
	workspaceName: Optional[str] = Field(alias="workspaceName",default=None,)

from .windows_updates_resource_connection_state import WindowsUpdatesResourceConnectionState

