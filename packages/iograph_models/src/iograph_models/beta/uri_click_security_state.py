from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UriClickSecurityState(BaseModel):
	clickAction: Optional[str] = Field(alias="clickAction", default=None,)
	clickDateTime: Optional[datetime] = Field(alias="clickDateTime", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	uriDomain: Optional[str] = Field(alias="uriDomain", default=None,)
	verdict: Optional[str] = Field(alias="verdict", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

