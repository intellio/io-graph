from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Security_aggregated_apps_details_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecurityEndpointDiscoveredCloudAppDetail],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_endpoint_discovered_cloud_app_detail import SecurityEndpointDiscoveredCloudAppDetail

