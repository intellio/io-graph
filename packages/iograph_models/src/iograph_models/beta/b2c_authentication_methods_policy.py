from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class B2cAuthenticationMethodsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.b2cAuthenticationMethodsPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.b2cAuthenticationMethodsPolicy")
	isEmailPasswordAuthenticationEnabled: Optional[bool] = Field(alias="isEmailPasswordAuthenticationEnabled", default=None,)
	isPhoneOneTimePasswordAuthenticationEnabled: Optional[bool] = Field(alias="isPhoneOneTimePasswordAuthenticationEnabled", default=None,)
	isUserNameAuthenticationEnabled: Optional[bool] = Field(alias="isUserNameAuthenticationEnabled", default=None,)

