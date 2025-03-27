from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdatePostRequest(BaseModel):
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	months: Optional[str] = Field(alias="months", default=None,)


