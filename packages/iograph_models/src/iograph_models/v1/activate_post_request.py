from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ActivatePostRequest(BaseModel):
	effectiveDateTime: Optional[datetime] = Field(alias="effectiveDateTime", default=None,)


