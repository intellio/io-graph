from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentitySecurityDefaultsEnforcementPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[IdentitySecurityDefaultsEnforcementPolicy]] = Field(alias="value",default=None,)

from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy

