from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnInteractiveAuthFlowStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OnInteractiveAuthFlowStartListener] = Field(alias="value",)

from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener

