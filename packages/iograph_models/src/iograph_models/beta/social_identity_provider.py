from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SocialIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	clientId: Optional[str] = Field(alias="clientId",default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret",default=None,)
	identityProviderType: Optional[str] = Field(alias="identityProviderType",default=None,)


