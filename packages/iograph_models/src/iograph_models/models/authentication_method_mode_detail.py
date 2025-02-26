from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationMethodModeDetail(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationMethod: Optional[BaseAuthenticationMethod] = Field(default=None,alias="authenticationMethod",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)

from .base_authentication_method import BaseAuthenticationMethod

