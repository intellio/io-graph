from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Fido2CombinationConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appliesToCombinations: Optional[list[AuthenticationMethodModes]] = Field(default=None,alias="appliesToCombinations",)
	allowedAAGUIDs: Optional[list[str]] = Field(default=None,alias="allowedAAGUIDs",)

from .authentication_method_modes import AuthenticationMethodModes

