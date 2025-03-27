from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InferenceClassification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	overrides: Optional[list[InferenceClassificationOverride]] = Field(alias="overrides", default=None,)

from .inference_classification_override import InferenceClassificationOverride

