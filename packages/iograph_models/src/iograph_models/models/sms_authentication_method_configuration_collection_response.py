from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SmsAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SmsAuthenticationMethodConfiguration] = Field(alias="value",)

from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration

