from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InferenceClassificationOverride(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	classifyAs: Optional[InferenceClassificationType | str] = Field(alias="classifyAs", default=None,)
	senderEmailAddress: Optional[EmailAddress] = Field(alias="senderEmailAddress", default=None,)

from .inference_classification_type import InferenceClassificationType
from .email_address import EmailAddress

