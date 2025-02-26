from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationStrengthUsage(BaseModel):
	mfa: list[ConditionalAccessPolicy] = Field(alias="mfa",)
	none: list[ConditionalAccessPolicy] = Field(alias="none",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_policy import ConditionalAccessPolicy
from .conditional_access_policy import ConditionalAccessPolicy

