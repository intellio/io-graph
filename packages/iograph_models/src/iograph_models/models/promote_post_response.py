from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PromotePostResponse(BaseModel):
	value: Optional[bool] = Field(default=None,alias="value",)


