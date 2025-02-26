from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultInvitationRedemptionIdentityProviderConfiguration(BaseModel):
	fallbackIdentityProvider: Optional[B2bIdentityProvidersType] = Field(default=None,alias="fallbackIdentityProvider",)
	primaryIdentityProviderPrecedenceOrder: Optional[B2bIdentityProvidersType] = Field(default=None,alias="primaryIdentityProviderPrecedenceOrder",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .b2b_identity_providers_type import B2bIdentityProvidersType
from .b2b_identity_providers_type import B2bIdentityProvidersType

