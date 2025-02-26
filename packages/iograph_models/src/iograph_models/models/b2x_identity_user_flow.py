from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class B2xIdentityUserFlow(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userFlowType: Optional[UserFlowType] = Field(default=None,alias="userFlowType",)
	userFlowTypeVersion: Optional[float] | Optional[str] | ReferenceNumeric
	apiConnectorConfiguration: Optional[UserFlowApiConnectorConfiguration] = Field(default=None,alias="apiConnectorConfiguration",)
	identityProviders: list[IdentityProvider] = Field(alias="identityProviders",)
	languages: list[UserFlowLanguageConfiguration] = Field(alias="languages",)
	userAttributeAssignments: list[IdentityUserFlowAttributeAssignment] = Field(alias="userAttributeAssignments",)
	userFlowIdentityProviders: list[IdentityProviderBase] = Field(alias="userFlowIdentityProviders",)

from .user_flow_type import UserFlowType
from .reference_numeric import ReferenceNumeric
from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
from .identity_provider import IdentityProvider
from .user_flow_language_configuration import UserFlowLanguageConfiguration
from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
from .identity_provider_base import IdentityProviderBase

