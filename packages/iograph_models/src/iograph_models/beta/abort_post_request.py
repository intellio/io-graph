from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AbortPostRequest(BaseModel):
	reason: Optional[str] = Field(alias="reason",default=None,)


