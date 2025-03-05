from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdateAllowedCombinationsResult(BaseModel):
	additionalInformation: Optional[str] = Field(default=None,alias="additionalInformation",)
	conditionalAccessReferences: Optional[list[str]] = Field(default=None,alias="conditionalAccessReferences",)
	currentCombinations: Optional[list[AuthenticationMethodModes]] = Field(default=None,alias="currentCombinations",)
	previousCombinations: Optional[list[AuthenticationMethodModes]] = Field(default=None,alias="previousCombinations",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_method_modes import AuthenticationMethodModes

