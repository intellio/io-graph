from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationStrengthUsage(BaseModel):
	mfa: Optional[list[ConditionalAccessPolicy]] = Field(alias="mfa", default=None,)
	none: Optional[list[ConditionalAccessPolicy]] = Field(alias="none", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_policy import ConditionalAccessPolicy
from .conditional_access_policy import ConditionalAccessPolicy

