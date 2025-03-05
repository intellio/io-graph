from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	apiConnectors: Optional[list[IdentityApiConnector]] = Field(default=None,alias="apiConnectors",)
	authenticationEventListeners: SerializeAsAny[Optional[list[AuthenticationEventListener]]] = Field(default=None,alias="authenticationEventListeners",)
	authenticationEventsFlows: SerializeAsAny[Optional[list[AuthenticationEventsFlow]]] = Field(default=None,alias="authenticationEventsFlows",)
	b2xUserFlows: Optional[list[B2xIdentityUserFlow]] = Field(default=None,alias="b2xUserFlows",)
	conditionalAccess: Optional[ConditionalAccessRoot] = Field(default=None,alias="conditionalAccess",)
	customAuthenticationExtensions: SerializeAsAny[Optional[list[CustomAuthenticationExtension]]] = Field(default=None,alias="customAuthenticationExtensions",)
	identityProviders: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(default=None,alias="identityProviders",)
	userFlowAttributes: SerializeAsAny[Optional[list[IdentityUserFlowAttribute]]] = Field(default=None,alias="userFlowAttributes",)

from .identity_api_connector import IdentityApiConnector
from .authentication_event_listener import AuthenticationEventListener
from .authentication_events_flow import AuthenticationEventsFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow
from .conditional_access_root import ConditionalAccessRoot
from .custom_authentication_extension import CustomAuthenticationExtension
from .identity_provider_base import IdentityProviderBase
from .identity_user_flow_attribute import IdentityUserFlowAttribute

