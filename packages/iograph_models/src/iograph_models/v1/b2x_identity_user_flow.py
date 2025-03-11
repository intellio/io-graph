from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class B2xIdentityUserFlow(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userFlowType: Optional[UserFlowType | str] = Field(alias="userFlowType",default=None,)
	userFlowTypeVersion: float | str | ReferenceNumeric
	apiConnectorConfiguration: Optional[UserFlowApiConnectorConfiguration] = Field(alias="apiConnectorConfiguration",default=None,)
	identityProviders: Optional[list[IdentityProvider]] = Field(alias="identityProviders",default=None,)
	languages: Optional[list[UserFlowLanguageConfiguration]] = Field(alias="languages",default=None,)
	userAttributeAssignments: Optional[list[IdentityUserFlowAttributeAssignment]] = Field(alias="userAttributeAssignments",default=None,)
	userFlowIdentityProviders: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(alias="userFlowIdentityProviders",default=None,)

from .user_flow_type import UserFlowType
from .reference_numeric import ReferenceNumeric
from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
from .identity_provider import IdentityProvider
from .user_flow_language_configuration import UserFlowLanguageConfiguration
from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
from .identity_provider_base import IdentityProviderBase

