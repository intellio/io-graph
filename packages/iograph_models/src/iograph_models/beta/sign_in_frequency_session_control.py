from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SignInFrequencySessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.signInFrequencySessionControl"] = Field(alias="@odata.type", default="#microsoft.graph.signInFrequencySessionControl")
	authenticationType: Optional[SignInFrequencyAuthenticationType | str] = Field(alias="authenticationType", default=None,)
	frequencyInterval: Optional[SignInFrequencyInterval | str] = Field(alias="frequencyInterval", default=None,)
	type: Optional[SigninFrequencyType | str] = Field(alias="type", default=None,)
	value: Optional[int] = Field(alias="value", default=None,)

from .sign_in_frequency_authentication_type import SignInFrequencyAuthenticationType
from .sign_in_frequency_interval import SignInFrequencyInterval
from .signin_frequency_type import SigninFrequencyType
