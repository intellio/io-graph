from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_permissionPostRequest(BaseModel):
	challengeToken: Optional[str] = Field(alias="challengeToken",default=None,)
	password: Optional[str] = Field(alias="password",default=None,)


