from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class InferenceClassificationOverride(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.inferenceClassificationOverride"] = Field(alias="@odata.type", default="#microsoft.graph.inferenceClassificationOverride")
	classifyAs: Optional[InferenceClassificationType | str] = Field(alias="classifyAs", default=None,)
	senderEmailAddress: Optional[Union[TypedEmailAddress]] = Field(alias="senderEmailAddress", default=None,discriminator="odata_type", )

from .inference_classification_type import InferenceClassificationType
from .typed_email_address import TypedEmailAddress
