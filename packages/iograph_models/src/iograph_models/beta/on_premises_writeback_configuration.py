from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesWritebackConfiguration(BaseModel):
	unifiedGroupContainer: Optional[str] = Field(alias="unifiedGroupContainer", default=None,)
	userContainer: Optional[str] = Field(alias="userContainer", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

