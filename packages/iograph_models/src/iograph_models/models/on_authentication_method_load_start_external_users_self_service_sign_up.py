from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	identityProviders: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(default=None,alias="identityProviders",)

from .identity_provider_base import IdentityProviderBase

