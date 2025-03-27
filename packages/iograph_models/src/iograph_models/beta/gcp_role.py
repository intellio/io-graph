from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GcpRole(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	gcpRoleType: Optional[GcpRoleType | str] = Field(alias="gcpRoleType", default=None,)
	scopes: Optional[list[GcpScope]] = Field(alias="scopes", default=None,)

from .gcp_role_type import GcpRoleType
from .gcp_scope import GcpScope

