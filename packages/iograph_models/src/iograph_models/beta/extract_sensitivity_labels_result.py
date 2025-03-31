from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExtractSensitivityLabelsResult(BaseModel):
	labels: Optional[list[SensitivityLabelAssignment]] = Field(alias="labels", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sensitivity_label_assignment import SensitivityLabelAssignment
