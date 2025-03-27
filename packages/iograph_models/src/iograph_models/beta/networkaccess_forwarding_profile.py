from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.forwardingProfile"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.forwardingProfile")
	description: Optional[str] = Field(alias="description", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policies: Optional[list[Annotated[Union[NetworkaccessFilteringPolicyLink, NetworkaccessForwardingPolicyLink],Field(discriminator="odata_type")]]] = Field(alias="policies", default=None,)
	associations: Optional[list[Annotated[Union[NetworkaccessAssociatedBranch],Field(discriminator="odata_type")]]] = Field(alias="associations", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	trafficForwardingType: Optional[NetworkaccessTrafficForwardingType | str] = Field(alias="trafficForwardingType", default=None,)
	servicePrincipal: Optional[ServicePrincipal] = Field(alias="servicePrincipal", default=None,)

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_filtering_policy_link import NetworkaccessFilteringPolicyLink
from .networkaccess_forwarding_policy_link import NetworkaccessForwardingPolicyLink
from .networkaccess_associated_branch import NetworkaccessAssociatedBranch
from .networkaccess_traffic_forwarding_type import NetworkaccessTrafficForwardingType
from .service_principal import ServicePrincipal

