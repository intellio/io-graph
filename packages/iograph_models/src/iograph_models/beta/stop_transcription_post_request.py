from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Stop_transcriptionPostRequest(BaseModel):
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)
	language: Optional[str] = Field(alias="language",default=None,)


