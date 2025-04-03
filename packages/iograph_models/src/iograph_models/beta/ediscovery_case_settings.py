from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EdiscoveryCaseSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ediscovery.caseSettings"] = Field(alias="@odata.type", default="#microsoft.graph.ediscovery.caseSettings")
	ocr: Optional[EdiscoveryOcrSettings] = Field(alias="ocr", default=None,)
	redundancyDetection: Optional[EdiscoveryRedundancyDetectionSettings] = Field(alias="redundancyDetection", default=None,)
	topicModeling: Optional[EdiscoveryTopicModelingSettings] = Field(alias="topicModeling", default=None,)

from .ediscovery_ocr_settings import EdiscoveryOcrSettings
from .ediscovery_redundancy_detection_settings import EdiscoveryRedundancyDetectionSettings
from .ediscovery_topic_modeling_settings import EdiscoveryTopicModelingSettings
