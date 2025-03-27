from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityOrganizationalScope(BaseModel):
	scopeNames: Optional[list[str]] = Field(alias="scopeNames", default=None,)
	scopeType: Optional[SecurityScopeType | str] = Field(alias="scopeType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_scope_type import SecurityScopeType

