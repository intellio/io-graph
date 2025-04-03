from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuthenticationMethodModeDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationMethodModeDetail"] = Field(alias="@odata.type", default="#microsoft.graph.authenticationMethodModeDetail")
	authenticationMethod: Optional[BaseAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

from .base_authentication_method import BaseAuthenticationMethod
