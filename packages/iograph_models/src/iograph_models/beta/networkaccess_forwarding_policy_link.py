from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingPolicyLink(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.forwardingPolicyLink"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.forwardingPolicyLink")
	state: Optional[NetworkaccessStatus | str] = Field(alias="state", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policy: Optional[Union[NetworkaccessFilteringPolicy, NetworkaccessForwardingPolicy]] = Field(alias="policy", default=None,discriminator="odata_type", )

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy
from .networkaccess_forwarding_policy import NetworkaccessForwardingPolicy

