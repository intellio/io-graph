from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CheckinPostRequest(BaseModel):
	checkInAs: Optional[str] = Field(default=None,alias="checkInAs",)
	comment: Optional[str] = Field(default=None,alias="comment",)


