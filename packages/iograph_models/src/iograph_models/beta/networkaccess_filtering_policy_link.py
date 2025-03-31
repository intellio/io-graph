from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkaccessFilteringPolicyLink(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.filteringPolicyLink"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.filteringPolicyLink")
	state: Optional[NetworkaccessStatus | str] = Field(alias="state", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policy: Optional[Union[NetworkaccessFilteringPolicy, NetworkaccessForwardingPolicy]] = Field(alias="policy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	loggingState: Optional[NetworkaccessStatus | str] = Field(alias="loggingState", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy
from .networkaccess_forwarding_policy import NetworkaccessForwardingPolicy
