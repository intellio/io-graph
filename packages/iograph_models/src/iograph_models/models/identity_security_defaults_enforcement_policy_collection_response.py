from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentitySecurityDefaultsEnforcementPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[IdentitySecurityDefaultsEnforcementPolicy]] = Field(default=None,alias="value",)

from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy

