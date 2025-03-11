from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CheckinPostRequest(BaseModel):
	checkInAs: Optional[str] = Field(alias="checkInAs",default=None,)
	comment: Optional[str] = Field(alias="comment",default=None,)


