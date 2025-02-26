from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInFrequencySessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationType: Optional[SignInFrequencyAuthenticationType] = Field(default=None,alias="authenticationType",)
	frequencyInterval: Optional[SignInFrequencyInterval] = Field(default=None,alias="frequencyInterval",)
	type: Optional[SigninFrequencyType] = Field(default=None,alias="type",)
	value: Optional[int] = Field(default=None,alias="value",)

from .sign_in_frequency_authentication_type import SignInFrequencyAuthenticationType
from .sign_in_frequency_interval import SignInFrequencyInterval
from .signin_frequency_type import SigninFrequencyType

