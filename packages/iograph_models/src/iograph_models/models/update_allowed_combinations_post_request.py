from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_allowed_combinationsPostRequest(BaseModel):
	allowedCombinations: Optional[AuthenticationMethodModes] = Field(default=None,alias="allowedCombinations",)

from .authentication_method_modes import AuthenticationMethodModes

