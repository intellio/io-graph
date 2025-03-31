from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkaccessFilteringProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.filteringProfile"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.filteringProfile")
	description: Optional[str] = Field(alias="description", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	policies: Optional[list[Annotated[Union[NetworkaccessFilteringPolicyLink, NetworkaccessForwardingPolicyLink],Field(discriminator="odata_type")]]] = Field(alias="policies", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	conditionalAccessPolicies: Optional[list[NetworkaccessConditionalAccessPolicy]] = Field(alias="conditionalAccessPolicies", default=None,)

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_filtering_policy_link import NetworkaccessFilteringPolicyLink
from .networkaccess_forwarding_policy_link import NetworkaccessForwardingPolicyLink
from .networkaccess_conditional_access_policy import NetworkaccessConditionalAccessPolicy
