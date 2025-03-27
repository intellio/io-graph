from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_passwordPostRequest(BaseModel):
	password: Optional[str] = Field(alias="password", default=None,)


