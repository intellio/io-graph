from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_solid_colorPostRequest(BaseModel):
	color: Optional[str] = Field(alias="color", default=None,)


