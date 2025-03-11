from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class B2cAuthenticationMethodsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isEmailPasswordAuthenticationEnabled: Optional[bool] = Field(alias="isEmailPasswordAuthenticationEnabled",default=None,)
	isPhoneOneTimePasswordAuthenticationEnabled: Optional[bool] = Field(alias="isPhoneOneTimePasswordAuthenticationEnabled",default=None,)
	isUserNameAuthenticationEnabled: Optional[bool] = Field(alias="isUserNameAuthenticationEnabled",default=None,)


