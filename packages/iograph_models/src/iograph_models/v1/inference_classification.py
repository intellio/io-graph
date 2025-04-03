from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InferenceClassification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.inferenceClassification"] = Field(alias="@odata.type", default="#microsoft.graph.inferenceClassification")
	overrides: Optional[list[InferenceClassificationOverride]] = Field(alias="overrides", default=None,)

from .inference_classification_override import InferenceClassificationOverride
