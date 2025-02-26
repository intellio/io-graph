from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchPostRequest(BaseModel):
	protectionUnitIds: list[Optional[str]] = Field(alias="protectionUnitIds",)
	protectionTimePeriod: Optional[TimePeriod] = Field(default=None,alias="protectionTimePeriod",)
	restorePointPreference: Optional[RestorePointPreference] = Field(default=None,alias="restorePointPreference",)
	tags: Optional[RestorePointTags] = Field(default=None,alias="tags",)
	artifactQuery: Optional[ArtifactQuery] = Field(default=None,alias="artifactQuery",)

from .time_period import TimePeriod
from .restore_point_preference import RestorePointPreference
from .restore_point_tags import RestorePointTags
from .artifact_query import ArtifactQuery

