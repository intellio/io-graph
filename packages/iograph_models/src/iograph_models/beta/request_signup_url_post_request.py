from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Request_signup_urlPostRequest(BaseModel):
	hostName: Optional[str] = Field(alias="hostName",default=None,)


