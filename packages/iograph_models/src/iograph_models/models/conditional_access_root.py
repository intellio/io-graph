from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationContextClassReferences: Optional[list[AuthenticationContextClassReference]] = Field(default=None,alias="authenticationContextClassReferences",)
	authenticationStrength: Optional[AuthenticationStrengthRoot] = Field(default=None,alias="authenticationStrength",)
	namedLocations: SerializeAsAny[Optional[list[NamedLocation]]] = Field(default=None,alias="namedLocations",)
	policies: Optional[list[ConditionalAccessPolicy]] = Field(default=None,alias="policies",)
	templates: Optional[list[ConditionalAccessTemplate]] = Field(default=None,alias="templates",)

from .authentication_context_class_reference import AuthenticationContextClassReference
from .authentication_strength_root import AuthenticationStrengthRoot
from .named_location import NamedLocation
from .conditional_access_policy import ConditionalAccessPolicy
from .conditional_access_template import ConditionalAccessTemplate

