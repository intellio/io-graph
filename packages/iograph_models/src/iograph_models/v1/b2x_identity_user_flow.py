from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class B2xIdentityUserFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.b2xIdentityUserFlow"] = Field(alias="@odata.type", default="#microsoft.graph.b2xIdentityUserFlow")
	userFlowType: Optional[UserFlowType | str] = Field(alias="userFlowType", default=None,)
	userFlowTypeVersion: float | str | ReferenceNumeric
	apiConnectorConfiguration: Optional[UserFlowApiConnectorConfiguration] = Field(alias="apiConnectorConfiguration", default=None,)
	identityProviders: Optional[list[IdentityProvider]] = Field(alias="identityProviders", default=None,)
	languages: Optional[list[UserFlowLanguageConfiguration]] = Field(alias="languages", default=None,)
	userAttributeAssignments: Optional[list[IdentityUserFlowAttributeAssignment]] = Field(alias="userAttributeAssignments", default=None,)
	userFlowIdentityProviders: Optional[list[Annotated[Union[AppleManagedIdentityProvider, BuiltInIdentityProvider, InternalDomainFederation, SamlOrWsFedExternalDomainFederation, SocialIdentityProvider],Field(discriminator="odata_type")]]] = Field(alias="userFlowIdentityProviders", default=None,)

from .user_flow_type import UserFlowType
from .reference_numeric import ReferenceNumeric
from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
from .identity_provider import IdentityProvider
from .user_flow_language_configuration import UserFlowLanguageConfiguration
from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
from .apple_managed_identity_provider import AppleManagedIdentityProvider
from .built_in_identity_provider import BuiltInIdentityProvider
from .internal_domain_federation import InternalDomainFederation
from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
from .social_identity_provider import SocialIdentityProvider
