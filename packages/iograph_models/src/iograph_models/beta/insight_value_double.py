from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class InsightValueDouble(BaseModel):
	odata_type: Literal["#microsoft.graph.insightValueDouble"] = Field(alias="@odata.type", default="#microsoft.graph.insightValueDouble")
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

