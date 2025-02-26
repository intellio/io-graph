from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Validate_permissionPostRequest(BaseModel):
	challengeToken: Optional[str] = Field(default=None,alias="challengeToken",)
	password: Optional[str] = Field(default=None,alias="password",)


