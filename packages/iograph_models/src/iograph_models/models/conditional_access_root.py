from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationContextClassReferences: list[AuthenticationContextClassReference] = Field(alias="authenticationContextClassReferences",)
	authenticationStrength: Optional[AuthenticationStrengthRoot] = Field(default=None,alias="authenticationStrength",)
	namedLocations: list[NamedLocation] = Field(alias="namedLocations",)
	policies: list[ConditionalAccessPolicy] = Field(alias="policies",)
	templates: list[ConditionalAccessTemplate] = Field(alias="templates",)

from .authentication_context_class_reference import AuthenticationContextClassReference
from .authentication_strength_root import AuthenticationStrengthRoot
from .named_location import NamedLocation
from .conditional_access_policy import ConditionalAccessPolicy
from .conditional_access_template import ConditionalAccessTemplate

