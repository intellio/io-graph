from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Mark_as_junkPostRequest(BaseModel):
	MoveToJunk: Optional[bool] = Field(alias="MoveToJunk", default=None,)


