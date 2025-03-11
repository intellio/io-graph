from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SmsAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SmsAuthenticationMethodConfiguration]] = Field(alias="value",default=None,)

from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration

