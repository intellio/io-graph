from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_priorityPostRequest(BaseModel):
	priority: Optional[int] = Field(alias="priority", default=None,)


