from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SocialIdentityProvider(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	clientId: Optional[str] = Field(default=None,alias="clientId",)
	clientSecret: Optional[str] = Field(default=None,alias="clientSecret",)
	identityProviderType: Optional[str] = Field(default=None,alias="identityProviderType",)


