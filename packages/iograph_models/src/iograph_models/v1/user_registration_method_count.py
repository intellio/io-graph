from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationMethodCount(BaseModel):
	authenticationMethod: Optional[str] = Field(alias="authenticationMethod", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


