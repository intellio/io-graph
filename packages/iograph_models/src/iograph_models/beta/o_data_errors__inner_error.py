from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ODataErrorsInnerError(BaseModel):
	request_id: Optional[str] = Field(alias="request-id",default=None,)
	client_request_id: Optional[str] = Field(alias="client-request-id",default=None,)
	date: Optional[datetime] = Field(alias="date",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


