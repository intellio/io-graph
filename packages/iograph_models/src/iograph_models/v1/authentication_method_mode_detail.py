from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodModeDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authenticationMethod: Optional[BaseAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

from .base_authentication_method import BaseAuthenticationMethod

