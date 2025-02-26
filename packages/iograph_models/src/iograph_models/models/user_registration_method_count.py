from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserRegistrationMethodCount(BaseModel):
	authenticationMethod: Optional[str] = Field(default=None,alias="authenticationMethod",)
	userCount: Optional[int] = Field(default=None,alias="userCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


