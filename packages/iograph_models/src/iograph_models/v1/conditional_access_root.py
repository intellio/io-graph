from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationContextClassReferences: Optional[list[AuthenticationContextClassReference]] = Field(alias="authenticationContextClassReferences",default=None,)
	authenticationStrength: Optional[AuthenticationStrengthRoot] = Field(alias="authenticationStrength",default=None,)
	namedLocations: SerializeAsAny[Optional[list[NamedLocation]]] = Field(alias="namedLocations",default=None,)
	policies: Optional[list[ConditionalAccessPolicy]] = Field(alias="policies",default=None,)
	templates: Optional[list[ConditionalAccessTemplate]] = Field(alias="templates",default=None,)

from .authentication_context_class_reference import AuthenticationContextClassReference
from .authentication_strength_root import AuthenticationStrengthRoot
from .named_location import NamedLocation
from .conditional_access_policy import ConditionalAccessPolicy
from .conditional_access_template import ConditionalAccessTemplate

