from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppleVppTokenTroubleshootingEventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AppleVppTokenTroubleshootingEvent]] = Field(alias="value",default=None,)

from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent

