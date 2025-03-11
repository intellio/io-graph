from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ResponseStatus(BaseModel):
	response: Optional[ResponseType | str] = Field(alias="response",default=None,)
	time: Optional[datetime] = Field(alias="time",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .response_type import ResponseType

