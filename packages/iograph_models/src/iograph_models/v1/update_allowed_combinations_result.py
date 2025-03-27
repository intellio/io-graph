from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdateAllowedCombinationsResult(BaseModel):
	additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None,)
	conditionalAccessReferences: Optional[list[str]] = Field(alias="conditionalAccessReferences", default=None,)
	currentCombinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="currentCombinations", default=None,)
	previousCombinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="previousCombinations", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_method_modes import AuthenticationMethodModes

