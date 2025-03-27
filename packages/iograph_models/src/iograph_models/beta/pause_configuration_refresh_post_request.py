from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Pause_configuration_refreshPostRequest(BaseModel):
	pauseTimePeriodInMinutes: Optional[int] = Field(alias="pauseTimePeriodInMinutes", default=None,)


