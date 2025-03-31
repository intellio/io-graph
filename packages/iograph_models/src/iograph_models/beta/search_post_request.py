from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchPostRequest(BaseModel):
	protectionUnitIds: Optional[list[str]] = Field(alias="protectionUnitIds", default=None,)
	protectionTimePeriod: Optional[TimePeriod] = Field(alias="protectionTimePeriod", default=None,)
	restorePointPreference: Optional[RestorePointPreference | str] = Field(alias="restorePointPreference", default=None,)
	tags: Optional[RestorePointTags | str] = Field(alias="tags", default=None,)
	artifactQuery: Optional[ArtifactQuery] = Field(alias="artifactQuery", default=None,)

from .time_period import TimePeriod
from .restore_point_preference import RestorePointPreference
from .restore_point_tags import RestorePointTags
from .artifact_query import ArtifactQuery
