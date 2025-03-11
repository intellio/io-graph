from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	policies: SerializeAsAny[Optional[list[NetworkaccessPolicyLink]]] = Field(alias="policies",default=None,)
	associations: SerializeAsAny[Optional[list[NetworkaccessAssociation]]] = Field(alias="associations",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	trafficForwardingType: Optional[NetworkaccessTrafficForwardingType | str] = Field(alias="trafficForwardingType",default=None,)
	servicePrincipal: Optional[ServicePrincipal] = Field(alias="servicePrincipal",default=None,)

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_policy_link import NetworkaccessPolicyLink
from .networkaccess_association import NetworkaccessAssociation
from .networkaccess_traffic_forwarding_type import NetworkaccessTrafficForwardingType
from .service_principal import ServicePrincipal

