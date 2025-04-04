from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class ConditionalAccessRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.conditionalAccessRoot"] = Field(alias="@odata.type", default="#microsoft.graph.conditionalAccessRoot")
	authenticationContextClassReferences: Optional[list[AuthenticationContextClassReference]] = Field(alias="authenticationContextClassReferences", default=None,)
	authenticationStrength: Optional[AuthenticationStrengthRoot] = Field(alias="authenticationStrength", default=None,)
	authenticationStrengths: Optional[AuthenticationStrengthRoot] = Field(alias="authenticationStrengths", default=None,)
	namedLocations: Optional[list[Annotated[Union[CompliantNetworkNamedLocation, CountryNamedLocation, IpNamedLocation],Field(discriminator="odata_type")]]] = Field(alias="namedLocations", default=None,)
	policies: Optional[list[Annotated[Union[ConditionalAccessWhatIfPolicy],Field(discriminator="odata_type")]]] = Field(alias="policies", default=None,)
	templates: Optional[list[ConditionalAccessTemplate]] = Field(alias="templates", default=None,)

from .authentication_context_class_reference import AuthenticationContextClassReference
from .authentication_strength_root import AuthenticationStrengthRoot
from .compliant_network_named_location import CompliantNetworkNamedLocation
from .country_named_location import CountryNamedLocation
from .ip_named_location import IpNamedLocation
from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
from .conditional_access_template import ConditionalAccessTemplate
