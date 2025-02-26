from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityArticleIndicator(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	source: Optional[SecurityIndicatorSource] = Field(default=None,alias="source",)
	artifact: Optional[SecurityArtifact] = Field(default=None,alias="artifact",)

from .security_indicator_source import SecurityIndicatorSource
from .security_artifact import SecurityArtifact

