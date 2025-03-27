from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class BuiltInIdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.builtInIdentityProvider"] = Field(alias="@odata.type", default="#microsoft.graph.builtInIdentityProvider")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)
	state: Optional[IdentityProviderState | str] = Field(alias="state", default=None,)

from .identity_provider_state import IdentityProviderState

