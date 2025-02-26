from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	apiConnectors: list[IdentityApiConnector] = Field(alias="apiConnectors",)
	authenticationEventListeners: list[AuthenticationEventListener] = Field(alias="authenticationEventListeners",)
	authenticationEventsFlows: list[AuthenticationEventsFlow] = Field(alias="authenticationEventsFlows",)
	b2xUserFlows: list[B2xIdentityUserFlow] = Field(alias="b2xUserFlows",)
	conditionalAccess: Optional[ConditionalAccessRoot] = Field(default=None,alias="conditionalAccess",)
	customAuthenticationExtensions: list[CustomAuthenticationExtension] = Field(alias="customAuthenticationExtensions",)
	identityProviders: list[IdentityProviderBase] = Field(alias="identityProviders",)
	userFlowAttributes: list[IdentityUserFlowAttribute] = Field(alias="userFlowAttributes",)

from .identity_api_connector import IdentityApiConnector
from .authentication_event_listener import AuthenticationEventListener
from .authentication_events_flow import AuthenticationEventsFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow
from .conditional_access_root import ConditionalAccessRoot
from .custom_authentication_extension import CustomAuthenticationExtension
from .identity_provider_base import IdentityProviderBase
from .identity_user_flow_attribute import IdentityUserFlowAttribute

