from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SmsAuthenticationMethodTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SmsAuthenticationMethodTarget]] = Field(alias="value", default=None,)

from .sms_authentication_method_target import SmsAuthenticationMethodTarget

