from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class B2xIdentityUserFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	userFlowType: Optional[UserFlowType | str] = Field(alias="userFlowType", default=None,)
	userFlowTypeVersion: float | str | ReferenceNumeric
	apiConnectorConfiguration: Optional[UserFlowApiConnectorConfiguration] = Field(alias="apiConnectorConfiguration", default=None,)
	identityProviders: Optional[list[Annotated[Union[OpenIdConnectProvider]],Field(discriminator="odata_type")]]] = Field(alias="identityProviders", default=None,)
	languages: Optional[list[UserFlowLanguageConfiguration]] = Field(alias="languages", default=None,)
	userAttributeAssignments: Optional[list[IdentityUserFlowAttributeAssignment]] = Field(alias="userAttributeAssignments", default=None,)
	userFlowIdentityProviders: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, OidcIdentityProvider, OpenIdConnectIdentityProvider, SamlOrWsFedProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider]],Field(discriminator="odata_type")]]] = Field(alias="userFlowIdentityProviders", default=None,)

from .user_flow_type import UserFlowType
from .reference_numeric import ReferenceNumeric
from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
from .open_id_connect_provider import OpenIdConnectProvider
from .user_flow_language_configuration import UserFlowLanguageConfiguration
from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .oidc_identity_provider import OidcIdentityProvider
from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
from .saml_or_ws_fed_provider import SamlOrWsFedProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider

