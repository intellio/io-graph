from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class IdentityContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityContainer"] = Field(alias="@odata.type",)
	apiConnectors: Optional[list[IdentityApiConnector]] = Field(alias="apiConnectors", default=None,)
	authenticationEventListeners: Optional[list[Annotated[Union[OnAttributeCollectionListener, OnAuthenticationMethodLoadStartListener, OnInteractiveAuthFlowStartListener, OnTokenIssuanceStartListener, OnUserCreateStartListener],Field(discriminator="odata_type")]]] = Field(alias="authenticationEventListeners", default=None,)
	authenticationEventsFlows: Optional[list[Annotated[Union[ExternalUsersSelfServiceSignUpEventsFlow],Field(discriminator="odata_type")]]] = Field(alias="authenticationEventsFlows", default=None,)
	b2xUserFlows: Optional[list[B2xIdentityUserFlow]] = Field(alias="b2xUserFlows", default=None,)
	conditionalAccess: Optional[ConditionalAccessRoot] = Field(alias="conditionalAccess", default=None,)
	customAuthenticationExtensions: Optional[list[Annotated[Union[OnTokenIssuanceStartCustomExtension],Field(discriminator="odata_type")]]] = Field(alias="customAuthenticationExtensions", default=None,)
	identityProviders: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider],Field(discriminator="odata_type")]]] = Field(alias="identityProviders", default=None,)
	userFlowAttributes: Optional[list[Annotated[Union[IdentityBuiltInUserFlowAttribute, IdentityCustomUserFlowAttribute],Field(discriminator="odata_type")]]] = Field(alias="userFlowAttributes", default=None,)

from .identity_api_connector import IdentityApiConnector
from .on_attribute_collection_listener import OnAttributeCollectionListener
from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
from .on_user_create_start_listener import OnUserCreateStartListener
from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow
from .conditional_access_root import ConditionalAccessRoot
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider
from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
