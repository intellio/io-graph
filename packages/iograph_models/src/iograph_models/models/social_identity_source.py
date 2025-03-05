from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SocialIdentitySource(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	socialIdentitySourceType: Optional[str | SocialIdentitySourceType] = Field(alias="socialIdentitySourceType",default=None,)

from .social_identity_source_type import SocialIdentitySourceType

