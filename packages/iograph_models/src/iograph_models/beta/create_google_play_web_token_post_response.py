from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_google_play_web_tokenPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)


