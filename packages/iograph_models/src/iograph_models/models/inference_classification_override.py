from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InferenceClassificationOverride(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	classifyAs: Optional[InferenceClassificationType] = Field(default=None,alias="classifyAs",)
	senderEmailAddress: Optional[EmailAddress] = Field(default=None,alias="senderEmailAddress",)

from .inference_classification_type import InferenceClassificationType
from .email_address import EmailAddress

