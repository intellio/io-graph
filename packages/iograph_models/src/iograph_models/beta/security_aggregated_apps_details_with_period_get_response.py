from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_aggregated_apps_details_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[SecurityDiscoveredCloudAppDetail]]] = Field(alias="value",default=None,)

from .security_discovered_cloud_app_detail import SecurityDiscoveredCloudAppDetail

