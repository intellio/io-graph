from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InferenceClassificationOverrideCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[InferenceClassificationOverride] = Field(alias="value",)

from .inference_classification_override import InferenceClassificationOverride

