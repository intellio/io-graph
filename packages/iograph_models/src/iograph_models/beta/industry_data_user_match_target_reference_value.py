from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IndustryDataUserMatchTargetReferenceValue(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	value: Optional[IndustryDataReferenceDefinition] = Field(alias="value", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.userMatchTargetReferenceValue"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.userMatchTargetReferenceValue")

from .industry_data_reference_definition import IndustryDataReferenceDefinition
