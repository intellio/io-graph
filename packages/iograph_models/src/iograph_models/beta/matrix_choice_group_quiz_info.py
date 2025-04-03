from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class MatrixChoiceGroupQuizInfo(BaseModel):
	maxPoints: float | str | ReferenceNumeric
	odata_type: Literal["#microsoft.graph.matrixChoiceGroupQuizInfo"] = Field(alias="@odata.type", default="#microsoft.graph.matrixChoiceGroupQuizInfo")

from .reference_numeric import ReferenceNumeric
