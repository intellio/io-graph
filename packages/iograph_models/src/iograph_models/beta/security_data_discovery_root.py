from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDataDiscoveryRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudAppDiscovery: Optional[SecurityDataDiscoveryReport] = Field(alias="cloudAppDiscovery",default=None,)

from .security_data_discovery_report import SecurityDataDiscoveryReport

