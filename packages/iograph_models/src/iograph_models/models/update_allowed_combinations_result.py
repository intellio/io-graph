from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UpdateAllowedCombinationsResult(BaseModel):
	additionalInformation: Optional[str] = Field(default=None,alias="additionalInformation",)
	conditionalAccessReferences: list[Optional[str]] = Field(alias="conditionalAccessReferences",)
	currentCombinations: list[AuthenticationMethodModes] = Field(alias="currentCombinations",)
	previousCombinations: list[AuthenticationMethodModes] = Field(alias="previousCombinations",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_method_modes import AuthenticationMethodModes

