from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_allowed_combinationsPostRequest(BaseModel):
	allowedCombinations: Optional[AuthenticationMethodModes | str] = Field(alias="allowedCombinations",default=None,)

from .authentication_method_modes import AuthenticationMethodModes

