from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityContainer(BaseModel):
	apiConnectors: Optional[list[IdentityApiConnector]] = Field(alias="apiConnectors", default=None,)
	authenticationEventListeners: Optional[list[Annotated[Union[OnAttributeCollectionListener, OnAttributeCollectionStartListener, OnAttributeCollectionSubmitListener, OnAuthenticationMethodLoadStartListener, OnEmailOtpSendListener, OnInteractiveAuthFlowStartListener, OnPhoneMethodLoadStartListener, OnTokenIssuanceStartListener, OnUserCreateStartListener]],Field(discriminator="odata_type")]]] = Field(alias="authenticationEventListeners", default=None,)
	authenticationEventsFlows: Optional[list[Annotated[Union[ExternalUsersSelfServiceSignUpEventsFlow]],Field(discriminator="odata_type")]]] = Field(alias="authenticationEventsFlows", default=None,)
	b2cUserFlows: Optional[list[B2cIdentityUserFlow]] = Field(alias="b2cUserFlows", default=None,)
	b2xUserFlows: Optional[list[B2xIdentityUserFlow]] = Field(alias="b2xUserFlows", default=None,)
	conditionalAccess: Optional[ConditionalAccessRoot] = Field(alias="conditionalAccess", default=None,)
	continuousAccessEvaluationPolicy: Optional[ContinuousAccessEvaluationPolicy] = Field(alias="continuousAccessEvaluationPolicy", default=None,)
	customAuthenticationExtensions: Optional[list[Annotated[Union[OnAttributeCollectionStartCustomExtension, OnAttributeCollectionSubmitCustomExtension, OnOtpSendCustomExtension, OnTokenIssuanceStartCustomExtension]],Field(discriminator="odata_type")]]] = Field(alias="customAuthenticationExtensions", default=None,)
	identityProviders: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, OidcIdentityProvider, OpenIdConnectIdentityProvider, SamlOrWsFedProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider]],Field(discriminator="odata_type")]]] = Field(alias="identityProviders", default=None,)
	productChanges: Optional[list[Annotated[Union[Announcement, Roadmap]],Field(discriminator="odata_type")]]] = Field(alias="productChanges", default=None,)
	userFlowAttributes: Optional[list[Annotated[Union[IdentityBuiltInUserFlowAttribute, IdentityCustomUserFlowAttribute]],Field(discriminator="odata_type")]]] = Field(alias="userFlowAttributes", default=None,)
	userFlows: Optional[list[Annotated[Union[B2cIdentityUserFlow, B2xIdentityUserFlow]],Field(discriminator="odata_type")]]] = Field(alias="userFlows", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .identity_api_connector import IdentityApiConnector
from .on_attribute_collection_listener import OnAttributeCollectionListener
from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
from .on_email_otp_send_listener import OnEmailOtpSendListener
from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
from .on_phone_method_load_start_listener import OnPhoneMethodLoadStartListener
from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
from .on_user_create_start_listener import OnUserCreateStartListener
from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
from .b2c_identity_user_flow import B2cIdentityUserFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow
from .conditional_access_root import ConditionalAccessRoot
from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy
from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
from .on_otp_send_custom_extension import OnOtpSendCustomExtension
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .oidc_identity_provider import OidcIdentityProvider
from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
from .saml_or_ws_fed_provider import SamlOrWsFedProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider
from .announcement import Announcement
from .roadmap import Roadmap
from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
from .b2c_identity_user_flow import B2cIdentityUserFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow

