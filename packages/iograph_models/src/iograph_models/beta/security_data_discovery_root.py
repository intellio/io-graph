from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDataDiscoveryRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.dataDiscoveryRoot"] = Field(alias="@odata.type",)
	cloudAppDiscovery: Optional[SecurityDataDiscoveryReport] = Field(alias="cloudAppDiscovery", default=None,)

from .security_data_discovery_report import SecurityDataDiscoveryReport
