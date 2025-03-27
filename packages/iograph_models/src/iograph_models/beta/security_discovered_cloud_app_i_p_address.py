from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDiscoveredCloudAppIPAddress(BaseModel):
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


