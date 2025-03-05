from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SmsAuthenticationMethodTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SmsAuthenticationMethodTarget]] = Field(default=None,alias="value",)

from .sms_authentication_method_target import SmsAuthenticationMethodTarget

