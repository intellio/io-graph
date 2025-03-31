from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnPhoneMethodLoadStartExternalUsersAuthHandler(BaseModel):
	odata_type: Literal["#microsoft.graph.onPhoneMethodLoadStartExternalUsersAuthHandler"] = Field(alias="@odata.type", default="#microsoft.graph.onPhoneMethodLoadStartExternalUsersAuthHandler")
	smsOptions: Optional[PhoneOptions] = Field(alias="smsOptions", default=None,)
	voiceOptions: Optional[PhoneOptions] = Field(alias="voiceOptions", default=None,)

from .phone_options import PhoneOptions
