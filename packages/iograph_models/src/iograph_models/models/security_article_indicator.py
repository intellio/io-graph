from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityArticleIndicator(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	source: Optional[str | SecurityIndicatorSource] = Field(alias="source",default=None,)
	artifact: SerializeAsAny[Optional[SecurityArtifact]] = Field(alias="artifact",default=None,)

from .security_indicator_source import SecurityIndicatorSource
from .security_artifact import SecurityArtifact

