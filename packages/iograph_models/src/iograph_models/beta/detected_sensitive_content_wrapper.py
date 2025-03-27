from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DetectedSensitiveContentWrapper(BaseModel):
	classification: Optional[list[Annotated[Union[MachineLearningDetectedSensitiveContent],Field(discriminator="odata_type")]]] = Field(alias="classification", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

