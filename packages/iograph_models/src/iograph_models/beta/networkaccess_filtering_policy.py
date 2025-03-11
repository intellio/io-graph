from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessFilteringPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	policyRules: SerializeAsAny[Optional[list[NetworkaccessPolicyRule]]] = Field(alias="policyRules",default=None,)
	action: Optional[NetworkaccessFilteringPolicyAction | str] = Field(alias="action",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)

from .networkaccess_policy_rule import NetworkaccessPolicyRule
from .networkaccess_filtering_policy_action import NetworkaccessFilteringPolicyAction

