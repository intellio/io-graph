from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AppliedAuthenticationEventListener(BaseModel):
	eventType: Optional[AuthenticationEventType | str] = Field(alias="eventType", default=None,)
	executedListenerId: Optional[str] = Field(alias="executedListenerId", default=None,)
	handlerResult: Optional[Union[CustomExtensionCalloutResult]] = Field(alias="handlerResult", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_event_type import AuthenticationEventType
from .custom_extension_callout_result import CustomExtensionCalloutResult
