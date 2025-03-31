from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DefaultInvitationRedemptionIdentityProviderConfiguration(BaseModel):
	fallbackIdentityProvider: Optional[B2bIdentityProvidersType | str] = Field(alias="fallbackIdentityProvider", default=None,)
	primaryIdentityProviderPrecedenceOrder: Optional[list[B2bIdentityProvidersType | str]] = Field(alias="primaryIdentityProviderPrecedenceOrder", default=None,)
	odata_type: Literal["#microsoft.graph.defaultInvitationRedemptionIdentityProviderConfiguration"] = Field(alias="@odata.type",)

from .b2b_identity_providers_type import B2bIdentityProvidersType
