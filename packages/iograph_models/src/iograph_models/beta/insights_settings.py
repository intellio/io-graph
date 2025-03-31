from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InsightsSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.insightsSettings"] = Field(alias="@odata.type",)
	disabledForGroup: Optional[str] = Field(alias="disabledForGroup", default=None,)
	isEnabledInOrganization: Optional[bool] = Field(alias="isEnabledInOrganization", default=None,)

