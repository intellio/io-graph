from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Iso_week_numPostRequest(BaseModel):
	date: Optional[str] = Field(alias="date", default=None,)


