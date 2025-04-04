from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityCloudAppDiscoveryReportCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityCloudAppDiscoveryReport]] = Field(alias="value", default=None,)

from .security_cloud_app_discovery_report import SecurityCloudAppDiscoveryReport
