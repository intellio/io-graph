from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SocialIdentitySource(BaseModel):
	odata_type: Literal["#microsoft.graph.socialIdentitySource"] = Field(alias="@odata.type", default="#microsoft.graph.socialIdentitySource")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	socialIdentitySourceType: Optional[SocialIdentitySourceType | str] = Field(alias="socialIdentitySourceType", default=None,)

from .social_identity_source_type import SocialIdentitySourceType
