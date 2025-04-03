from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class NpsQuizInfo(BaseModel):
	maxPoints: float | str | ReferenceNumeric
	odata_type: Literal["#microsoft.graph.npsQuizInfo"] = Field(alias="@odata.type", default="#microsoft.graph.npsQuizInfo")

from .reference_numeric import ReferenceNumeric
