from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_google_play_web_tokenPostRequest(BaseModel):
	parentUri: Optional[str] = Field(alias="parentUri", default=None,)


