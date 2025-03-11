from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDetonationObservables(BaseModel):
	contactedIps: Optional[list[str]] = Field(alias="contactedIps",default=None,)
	contactedUrls: Optional[list[str]] = Field(alias="contactedUrls",default=None,)
	droppedfiles: Optional[list[str]] = Field(alias="droppedfiles",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


