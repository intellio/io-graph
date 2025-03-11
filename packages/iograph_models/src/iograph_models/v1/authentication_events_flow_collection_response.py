from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationEventsFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AuthenticationEventsFlow]]] = Field(alias="value",default=None,)

from .authentication_events_flow import AuthenticationEventsFlow

