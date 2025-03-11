from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIntelligenceProfileIndicator(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	source: Optional[SecurityIndicatorSource | str] = Field(alias="source",default=None,)
	artifact: SerializeAsAny[Optional[SecurityArtifact]] = Field(alias="artifact",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)

from .security_indicator_source import SecurityIndicatorSource
from .security_artifact import SecurityArtifact

