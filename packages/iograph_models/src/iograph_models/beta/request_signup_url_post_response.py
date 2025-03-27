from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Request_signup_urlPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)


