from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RemovePostRequest(BaseModel):
	value: Optional[list[Site]] = Field(alias="value",default=None,)

from .site import Site

