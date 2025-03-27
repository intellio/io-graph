from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnInteractiveAuthFlowStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OnInteractiveAuthFlowStartListener]] = Field(alias="value", default=None,)

from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener

