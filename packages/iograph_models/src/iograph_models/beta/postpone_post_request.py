from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PostponePostRequest(BaseModel):
	postponeUntilDateTime: Optional[datetime] = Field(alias="postponeUntilDateTime", default=None,)

