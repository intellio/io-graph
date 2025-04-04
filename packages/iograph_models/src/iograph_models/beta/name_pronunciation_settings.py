from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NamePronunciationSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.namePronunciationSettings"] = Field(alias="@odata.type", default="#microsoft.graph.namePronunciationSettings")
	isEnabledInOrganization: Optional[bool] = Field(alias="isEnabledInOrganization", default=None,)

