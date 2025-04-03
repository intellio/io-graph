from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityEdiscoveryCaseSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoveryCaseSettings"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoveryCaseSettings")
	ocr: Optional[SecurityOcrSettings] = Field(alias="ocr", default=None,)
	redundancyDetection: Optional[SecurityRedundancyDetectionSettings] = Field(alias="redundancyDetection", default=None,)
	topicModeling: Optional[SecurityTopicModelingSettings] = Field(alias="topicModeling", default=None,)

from .security_ocr_settings import SecurityOcrSettings
from .security_redundancy_detection_settings import SecurityRedundancyDetectionSettings
from .security_topic_modeling_settings import SecurityTopicModelingSettings
