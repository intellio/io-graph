from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ResponseStatus(BaseModel):
	response: Optional[ResponseType] = Field(default=None,alias="response",)
	time: Optional[datetime] = Field(default=None,alias="time",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .response_type import ResponseType

