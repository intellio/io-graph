from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchPostRequest(BaseModel):
	protectionUnitIds: Optional[list[str]] = Field(alias="protectionUnitIds",default=None,)
	protectionTimePeriod: Optional[TimePeriod] = Field(alias="protectionTimePeriod",default=None,)
	restorePointPreference: Optional[str | RestorePointPreference] = Field(alias="restorePointPreference",default=None,)
	tags: Optional[str | RestorePointTags] = Field(alias="tags",default=None,)
	artifactQuery: Optional[ArtifactQuery] = Field(alias="artifactQuery",default=None,)

from .time_period import TimePeriod
from .restore_point_preference import RestorePointPreference
from .restore_point_tags import RestorePointTags
from .artifact_query import ArtifactQuery

