from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_groupPostResponse(BaseModel):
	value: Optional[bool] = Field(default=None,alias="value",)


