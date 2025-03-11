from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPhoneMethodLoadStartExternalUsersAuthHandler(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	smsOptions: Optional[PhoneOptions] = Field(alias="smsOptions",default=None,)
	voiceOptions: Optional[PhoneOptions] = Field(alias="voiceOptions",default=None,)

from .phone_options import PhoneOptions
from .phone_options import PhoneOptions

