from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Stop_hold_musicPostRequest(BaseModel):
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)


