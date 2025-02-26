from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ODataErrorsInnerError(BaseModel):
	request_id: Optional[str] = Field(default=None,alias="request-id",)
	client_request_id: Optional[str] = Field(default=None,alias="client-request-id",)
	date: Optional[datetime] = Field(default=None,alias="date",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


