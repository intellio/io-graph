from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIntelligenceProfileIndicator(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	source: Optional[SecurityIndicatorSource] = Field(default=None,alias="source",)
	artifact: SerializeAsAny[Optional[SecurityArtifact]] = Field(default=None,alias="artifact",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)

from .security_indicator_source import SecurityIndicatorSource
from .security_artifact import SecurityArtifact

