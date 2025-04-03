from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TextClassificationRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.textClassificationRequest"] = Field(alias="@odata.type", default="#microsoft.graph.textClassificationRequest")
	contentMetaData: Optional[ClassificationRequestContentMetaData] = Field(alias="contentMetaData", default=None,)
	fileExtension: Optional[str] = Field(alias="fileExtension", default=None,)
	matchTolerancesToInclude: Optional[MlClassificationMatchTolerance | str] = Field(alias="matchTolerancesToInclude", default=None,)
	scopesToRun: Optional[SensitiveTypeScope | str] = Field(alias="scopesToRun", default=None,)
	sensitiveTypeIds: Optional[list[str]] = Field(alias="sensitiveTypeIds", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)

from .classification_request_content_meta_data import ClassificationRequestContentMetaData
from .ml_classification_match_tolerance import MlClassificationMatchTolerance
from .sensitive_type_scope import SensitiveTypeScope
