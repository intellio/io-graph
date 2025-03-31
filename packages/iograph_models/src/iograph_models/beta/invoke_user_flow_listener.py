from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InvokeUserFlowListener(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.invokeUserFlowListener"] = Field(alias="@odata.type", default="#microsoft.graph.invokeUserFlowListener")
	priority: Optional[int] = Field(alias="priority", default=None,)
	sourceFilter: Optional[AuthenticationSourceFilter] = Field(alias="sourceFilter", default=None,)
	userFlow: Optional[B2xIdentityUserFlow] = Field(alias="userFlow", default=None,)

from .authentication_source_filter import AuthenticationSourceFilter
from .b2x_identity_user_flow import B2xIdentityUserFlow
