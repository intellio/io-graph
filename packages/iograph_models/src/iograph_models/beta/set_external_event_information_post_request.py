from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_external_event_informationPostRequest(BaseModel):
	externalEventId: Optional[str] = Field(alias="externalEventId", default=None,)

