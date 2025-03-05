from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DefaultInvitationRedemptionIdentityProviderConfiguration(BaseModel):
	fallbackIdentityProvider: Optional[str | B2bIdentityProvidersType] = Field(alias="fallbackIdentityProvider",default=None,)
	primaryIdentityProviderPrecedenceOrder: Optional[str | B2bIdentityProvidersType] = Field(alias="primaryIdentityProviderPrecedenceOrder",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .b2b_identity_providers_type import B2bIdentityProvidersType
from .b2b_identity_providers_type import B2bIdentityProvidersType

