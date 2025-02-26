from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class B2xIdentityUserFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[B2xIdentityUserFlow] = Field(alias="value",)

from .b2x_identity_user_flow import B2xIdentityUserFlow

