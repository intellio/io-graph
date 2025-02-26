from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserRegistrationMethodCountCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserRegistrationMethodCount] = Field(alias="value",)

from .user_registration_method_count import UserRegistrationMethodCount

