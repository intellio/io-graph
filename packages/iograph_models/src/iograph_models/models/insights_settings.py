from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InsightsSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	disabledForGroup: Optional[str] = Field(default=None,alias="disabledForGroup",)
	isEnabledInOrganization: Optional[bool] = Field(default=None,alias="isEnabledInOrganization",)


