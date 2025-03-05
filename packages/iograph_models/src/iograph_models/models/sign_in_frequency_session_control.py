from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SignInFrequencySessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationType: Optional[str | SignInFrequencyAuthenticationType] = Field(alias="authenticationType",default=None,)
	frequencyInterval: Optional[str | SignInFrequencyInterval] = Field(alias="frequencyInterval",default=None,)
	type: Optional[str | SigninFrequencyType] = Field(alias="type",default=None,)
	value: Optional[int] = Field(alias="value",default=None,)

from .sign_in_frequency_authentication_type import SignInFrequencyAuthenticationType
from .sign_in_frequency_interval import SignInFrequencyInterval
from .signin_frequency_type import SigninFrequencyType

