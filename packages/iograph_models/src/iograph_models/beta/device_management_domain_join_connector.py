from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementDomainJoinConnector(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastConnectionDateTime: Optional[datetime] = Field(alias="lastConnectionDateTime",default=None,)
	state: Optional[DeviceManagementDomainJoinConnectorState | str] = Field(alias="state",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)

from .device_management_domain_join_connector_state import DeviceManagementDomainJoinConnectorState

