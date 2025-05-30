from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InvokeUserFlowListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[InvokeUserFlowListener]] = Field(alias="value", default=None,)

from .invoke_user_flow_listener import InvokeUserFlowListener
