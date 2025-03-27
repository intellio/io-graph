from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EvaluateLabelJobResultGroup(BaseModel):
	automatic: Optional[EvaluateLabelJobResult] = Field(alias="automatic", default=None,)
	recommended: Optional[EvaluateLabelJobResult] = Field(alias="recommended", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .evaluate_label_job_result import EvaluateLabelJobResult
from .evaluate_label_job_result import EvaluateLabelJobResult

