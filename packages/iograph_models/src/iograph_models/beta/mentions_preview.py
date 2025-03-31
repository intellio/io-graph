from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MentionsPreview(BaseModel):
	isMentioned: Optional[bool] = Field(alias="isMentioned", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

