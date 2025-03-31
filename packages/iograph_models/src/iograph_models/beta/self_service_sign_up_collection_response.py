from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SelfServiceSignUpCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SelfServiceSignUp]] = Field(alias="value", default=None,)

from .self_service_sign_up import SelfServiceSignUp
