from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDataDiscoveryReport(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	uploadedStreams: Optional[list[SecurityCloudAppDiscoveryReport]] = Field(alias="uploadedStreams",default=None,)

from .security_cloud_app_discovery_report import SecurityCloudAppDiscoveryReport

