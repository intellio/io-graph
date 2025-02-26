from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExtractSensitivityLabelsResult(BaseModel):
	labels: list[SensitivityLabelAssignment] = Field(alias="labels",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .sensitivity_label_assignment import SensitivityLabelAssignment

