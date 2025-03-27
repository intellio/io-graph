from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2CombinationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fido2CombinationConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.fido2CombinationConfiguration")
	appliesToCombinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="appliesToCombinations", default=None,)
	allowedAAGUIDs: Optional[list[str]] = Field(alias="allowedAAGUIDs", default=None,)

from .authentication_method_modes import AuthenticationMethodModes

