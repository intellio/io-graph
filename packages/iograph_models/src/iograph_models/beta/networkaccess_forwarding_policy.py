from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	policyRules: SerializeAsAny[Optional[list[NetworkaccessPolicyRule]]] = Field(alias="policyRules",default=None,)
	trafficForwardingType: Optional[NetworkaccessTrafficForwardingType | str] = Field(alias="trafficForwardingType",default=None,)

from .networkaccess_policy_rule import NetworkaccessPolicyRule
from .networkaccess_traffic_forwarding_type import NetworkaccessTrafficForwardingType

