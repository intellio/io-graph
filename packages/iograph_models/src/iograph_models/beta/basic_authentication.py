from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BasicAuthentication(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	password: Optional[str] = Field(alias="password",default=None,)
	username: Optional[str] = Field(alias="username",default=None,)


