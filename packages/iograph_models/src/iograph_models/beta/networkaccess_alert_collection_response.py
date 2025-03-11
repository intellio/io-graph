from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessAlertCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NetworkaccessAlert]] = Field(alias="value",default=None,)

from .networkaccess_alert import NetworkaccessAlert

