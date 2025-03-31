from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SocialIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.socialIdentityProvider"] = Field(alias="@odata.type", default="#microsoft.graph.socialIdentityProvider")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret", default=None,)
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)

