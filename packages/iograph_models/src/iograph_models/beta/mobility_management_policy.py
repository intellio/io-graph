from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MobilityManagementPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobilityManagementPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.mobilityManagementPolicy")
	appliesTo: Optional[PolicyScope | str] = Field(alias="appliesTo", default=None,)
	complianceUrl: Optional[str] = Field(alias="complianceUrl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	discoveryUrl: Optional[str] = Field(alias="discoveryUrl", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isValid: Optional[bool] = Field(alias="isValid", default=None,)
	termsOfUseUrl: Optional[str] = Field(alias="termsOfUseUrl", default=None,)
	includedGroups: Optional[list[Group]] = Field(alias="includedGroups", default=None,)

from .policy_scope import PolicyScope
from .group import Group
