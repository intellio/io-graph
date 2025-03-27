from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Literal["#microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp"] = Field(alias="@odata.type", default="#microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp")
	identityProviders: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, OidcIdentityProvider, OpenIdConnectIdentityProvider, SamlOrWsFedProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider]],Field(discriminator="odata_type")]]] = Field(alias="identityProviders", default=None,)

from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .oidc_identity_provider import OidcIdentityProvider
from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
from .saml_or_ws_fed_provider import SamlOrWsFedProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider

