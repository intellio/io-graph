from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class B2cIdentityUserFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[B2cIdentityUserFlow]] = Field(alias="value", default=None,)

from .b2c_identity_user_flow import B2cIdentityUserFlow
