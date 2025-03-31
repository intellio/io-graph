from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class IdentityProviderBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider
