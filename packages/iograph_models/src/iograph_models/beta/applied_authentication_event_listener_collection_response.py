from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppliedAuthenticationEventListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AppliedAuthenticationEventListener]] = Field(alias="value",default=None,)

from .applied_authentication_event_listener import AppliedAuthenticationEventListener

