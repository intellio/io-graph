from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identityProviders: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(alias="identityProviders",default=None,)

from .identity_provider_base import IdentityProviderBase

