from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SocialIdentitySource(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	socialIdentitySourceType: Optional[SocialIdentitySourceType] = Field(default=None,alias="socialIdentitySourceType",)

from .social_identity_source_type import SocialIdentitySourceType

