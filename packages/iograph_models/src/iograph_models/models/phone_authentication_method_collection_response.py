from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PhoneAuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PhoneAuthenticationMethod] = Field(alias="value",)

from .phone_authentication_method import PhoneAuthenticationMethod

