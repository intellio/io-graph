from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MachineLearningDetectedSensitiveContent(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	recommendedConfidence: Optional[int] = Field(alias="recommendedConfidence", default=None,)
	uniqueCount: Optional[int] = Field(alias="uniqueCount", default=None,)
	odata_type: Literal["#microsoft.graph.machineLearningDetectedSensitiveContent"] = Field(alias="@odata.type", default="#microsoft.graph.machineLearningDetectedSensitiveContent")
	classificationAttributes: Optional[list[ClassificationAttribute]] = Field(alias="classificationAttributes", default=None,)
	classificationMethod: Optional[ClassificationMethod | str] = Field(alias="classificationMethod", default=None,)
	matches: Optional[list[SensitiveContentLocation]] = Field(alias="matches", default=None,)
	scope: Optional[SensitiveTypeScope | str] = Field(alias="scope", default=None,)
	sensitiveTypeSource: Optional[SensitiveTypeSource | str] = Field(alias="sensitiveTypeSource", default=None,)
	matchTolerance: Optional[MlClassificationMatchTolerance | str] = Field(alias="matchTolerance", default=None,)
	modelVersion: Optional[str] = Field(alias="modelVersion", default=None,)

from .classification_attribute import ClassificationAttribute
from .classification_method import ClassificationMethod
from .sensitive_content_location import SensitiveContentLocation
from .sensitive_type_scope import SensitiveTypeScope
from .sensitive_type_source import SensitiveTypeSource
from .ml_classification_match_tolerance import MlClassificationMatchTolerance
