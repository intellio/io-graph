from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Mute_allPostRequest(BaseModel):
	participants: Optional[list[str]] = Field(alias="participants", default=None,)
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)


