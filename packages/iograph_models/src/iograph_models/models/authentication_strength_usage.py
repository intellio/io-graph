from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationStrengthUsage(BaseModel):
	mfa: Optional[list[ConditionalAccessPolicy]] = Field(default=None,alias="mfa",)
	none: Optional[list[ConditionalAccessPolicy]] = Field(default=None,alias="none",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_policy import ConditionalAccessPolicy
from .conditional_access_policy import ConditionalAccessPolicy

