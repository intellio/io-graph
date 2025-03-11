from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Subscribe_to_tonePostRequest(BaseModel):
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)


