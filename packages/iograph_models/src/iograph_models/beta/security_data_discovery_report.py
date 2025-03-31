from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDataDiscoveryReport(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.dataDiscoveryReport"] = Field(alias="@odata.type",)
	uploadedStreams: Optional[list[SecurityCloudAppDiscoveryReport]] = Field(alias="uploadedStreams", default=None,)

from .security_cloud_app_discovery_report import SecurityCloudAppDiscoveryReport
