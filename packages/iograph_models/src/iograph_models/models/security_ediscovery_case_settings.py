from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCaseSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	ocr: Optional[SecurityOcrSettings] = Field(default=None,alias="ocr",)
	redundancyDetection: Optional[SecurityRedundancyDetectionSettings] = Field(default=None,alias="redundancyDetection",)
	topicModeling: Optional[SecurityTopicModelingSettings] = Field(default=None,alias="topicModeling",)

from .security_ocr_settings import SecurityOcrSettings
from .security_redundancy_detection_settings import SecurityRedundancyDetectionSettings
from .security_topic_modeling_settings import SecurityTopicModelingSettings

