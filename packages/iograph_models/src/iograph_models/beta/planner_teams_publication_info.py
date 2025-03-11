from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTeamsPublicationInfo(BaseModel):
	creationSourceKind: Optional[PlannerCreationSourceKind | str] = Field(alias="creationSourceKind",default=None,)
	teamsPublicationInfo: Optional[PlannerTeamsPublicationInfo] = Field(alias="teamsPublicationInfo",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publicationId: Optional[str] = Field(alias="publicationId",default=None,)
	publishedToPlanId: Optional[str] = Field(alias="publishedToPlanId",default=None,)
	publishingTeamId: Optional[str] = Field(alias="publishingTeamId",default=None,)
	publishingTeamName: Optional[str] = Field(alias="publishingTeamName",default=None,)

from .planner_creation_source_kind import PlannerCreationSourceKind

