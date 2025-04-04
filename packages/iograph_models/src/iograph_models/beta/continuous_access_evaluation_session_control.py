from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContinuousAccessEvaluationSessionControl(BaseModel):
	mode: Optional[ContinuousAccessEvaluationMode | str] = Field(alias="mode", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .continuous_access_evaluation_mode import ContinuousAccessEvaluationMode
