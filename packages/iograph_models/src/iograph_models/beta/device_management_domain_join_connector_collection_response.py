from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementDomainJoinConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceManagementDomainJoinConnector]] = Field(alias="value",default=None,)

from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector

