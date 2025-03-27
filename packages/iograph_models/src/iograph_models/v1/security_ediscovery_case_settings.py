from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCaseSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	ocr: Optional[SecurityOcrSettings] = Field(alias="ocr", default=None,)
	redundancyDetection: Optional[SecurityRedundancyDetectionSettings] = Field(alias="redundancyDetection", default=None,)
	topicModeling: Optional[SecurityTopicModelingSettings] = Field(alias="topicModeling", default=None,)

from .security_ocr_settings import SecurityOcrSettings
from .security_redundancy_detection_settings import SecurityRedundancyDetectionSettings
from .security_topic_modeling_settings import SecurityTopicModelingSettings

