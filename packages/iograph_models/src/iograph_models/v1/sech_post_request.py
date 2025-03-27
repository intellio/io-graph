from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SechPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)


