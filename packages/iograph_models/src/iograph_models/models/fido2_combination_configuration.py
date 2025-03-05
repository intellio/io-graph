from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2CombinationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appliesToCombinations: Optional[list[str | AuthenticationMethodModes]] = Field(alias="appliesToCombinations",default=None,)
	allowedAAGUIDs: Optional[list[str]] = Field(alias="allowedAAGUIDs",default=None,)

from .authentication_method_modes import AuthenticationMethodModes

