from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GcpRole(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.gcpRole"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	gcpRoleType: Optional[GcpRoleType | str] = Field(alias="gcpRoleType", default=None,)
	scopes: Optional[list[GcpScope]] = Field(alias="scopes", default=None,)

from .gcp_role_type import GcpRoleType
from .gcp_scope import GcpScope
