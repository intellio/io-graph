from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityContainer(BaseModel):
	apiConnectors: Optional[list[IdentityApiConnector]] = Field(alias="apiConnectors",default=None,)
	authenticationEventListeners: SerializeAsAny[Optional[list[AuthenticationEventListener]]] = Field(alias="authenticationEventListeners",default=None,)
	authenticationEventsFlows: SerializeAsAny[Optional[list[AuthenticationEventsFlow]]] = Field(alias="authenticationEventsFlows",default=None,)
	b2cUserFlows: Optional[list[B2cIdentityUserFlow]] = Field(alias="b2cUserFlows",default=None,)
	b2xUserFlows: Optional[list[B2xIdentityUserFlow]] = Field(alias="b2xUserFlows",default=None,)
	conditionalAccess: Optional[ConditionalAccessRoot] = Field(alias="conditionalAccess",default=None,)
	continuousAccessEvaluationPolicy: Optional[ContinuousAccessEvaluationPolicy] = Field(alias="continuousAccessEvaluationPolicy",default=None,)
	customAuthenticationExtensions: SerializeAsAny[Optional[list[CustomAuthenticationExtension]]] = Field(alias="customAuthenticationExtensions",default=None,)
	identityProviders: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(alias="identityProviders",default=None,)
	productChanges: SerializeAsAny[Optional[list[ChangeItemBase]]] = Field(alias="productChanges",default=None,)
	userFlowAttributes: SerializeAsAny[Optional[list[IdentityUserFlowAttribute]]] = Field(alias="userFlowAttributes",default=None,)
	userFlows: SerializeAsAny[Optional[list[IdentityUserFlow]]] = Field(alias="userFlows",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_api_connector import IdentityApiConnector
from .authentication_event_listener import AuthenticationEventListener
from .authentication_events_flow import AuthenticationEventsFlow
from .b2c_identity_user_flow import B2cIdentityUserFlow
from .b2x_identity_user_flow import B2xIdentityUserFlow
from .conditional_access_root import ConditionalAccessRoot
from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy
from .custom_authentication_extension import CustomAuthenticationExtension
from .identity_provider_base import IdentityProviderBase
from .change_item_base import ChangeItemBase
from .identity_user_flow_attribute import IdentityUserFlowAttribute
from .identity_user_flow import IdentityUserFlow

