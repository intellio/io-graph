from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InferenceClassification(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	overrides: list[InferenceClassificationOverride] = Field(alias="overrides",)

from .inference_classification_override import InferenceClassificationOverride

