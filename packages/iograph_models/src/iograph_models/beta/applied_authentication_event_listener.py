from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppliedAuthenticationEventListener(BaseModel):
	eventType: Optional[AuthenticationEventType | str] = Field(alias="eventType",default=None,)
	executedListenerId: Optional[str] = Field(alias="executedListenerId",default=None,)
	handlerResult: SerializeAsAny[Optional[AuthenticationEventHandlerResult]] = Field(alias="handlerResult",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_event_type import AuthenticationEventType
from .authentication_event_handler_result import AuthenticationEventHandlerResult

