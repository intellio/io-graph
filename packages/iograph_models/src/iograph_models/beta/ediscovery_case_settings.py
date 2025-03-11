from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCaseSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	ocr: Optional[EdiscoveryOcrSettings] = Field(alias="ocr",default=None,)
	redundancyDetection: Optional[EdiscoveryRedundancyDetectionSettings] = Field(alias="redundancyDetection",default=None,)
	topicModeling: Optional[EdiscoveryTopicModelingSettings] = Field(alias="topicModeling",default=None,)

from .ediscovery_ocr_settings import EdiscoveryOcrSettings
from .ediscovery_redundancy_detection_settings import EdiscoveryRedundancyDetectionSettings
from .ediscovery_topic_modeling_settings import EdiscoveryTopicModelingSettings

