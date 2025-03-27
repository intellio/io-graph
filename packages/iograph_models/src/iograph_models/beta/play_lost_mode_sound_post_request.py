from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Play_lost_mode_soundPostRequest(BaseModel):
	durationInMinutes: Optional[str] = Field(alias="durationInMinutes", default=None,)


