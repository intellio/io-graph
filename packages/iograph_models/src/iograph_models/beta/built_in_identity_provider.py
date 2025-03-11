from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BuiltInIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	identityProviderType: Optional[str] = Field(alias="identityProviderType",default=None,)
	state: Optional[IdentityProviderState | str] = Field(alias="state",default=None,)

from .identity_provider_state import IdentityProviderState

