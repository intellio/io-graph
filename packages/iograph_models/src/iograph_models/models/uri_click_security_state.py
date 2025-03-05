from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UriClickSecurityState(BaseModel):
	clickAction: Optional[str] = Field(default=None,alias="clickAction",)
	clickDateTime: Optional[datetime] = Field(default=None,alias="clickDateTime",)
	id: Optional[str] = Field(default=None,alias="id",)
	sourceId: Optional[str] = Field(default=None,alias="sourceId",)
	uriDomain: Optional[str] = Field(default=None,alias="uriDomain",)
	verdict: Optional[str] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


