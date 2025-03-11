from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_alertsPostRequest(BaseModel):
	value: Optional[list[Alert]] = Field(alias="value",default=None,)

from .alert import Alert

