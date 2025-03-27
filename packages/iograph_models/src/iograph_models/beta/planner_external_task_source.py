from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerExternalTaskSource(BaseModel):
	creationSourceKind: Optional[PlannerCreationSourceKind | str] = Field(alias="creationSourceKind", default=None,)
	teamsPublicationInfo: Optional[PlannerTeamsPublicationInfo] = Field(alias="teamsPublicationInfo", default=None,)
	odata_type: Literal["#microsoft.graph.plannerExternalTaskSource"] = Field(alias="@odata.type", default="#microsoft.graph.plannerExternalTaskSource")
	contextScenarioId: Optional[str] = Field(alias="contextScenarioId", default=None,)
	displayLinkType: Optional[PlannerExternalTaskSourceDisplayType | str] = Field(alias="displayLinkType", default=None,)
	displayNameSegments: Optional[list[str]] = Field(alias="displayNameSegments", default=None,)
	externalContextId: Optional[str] = Field(alias="externalContextId", default=None,)
	externalObjectId: Optional[str] = Field(alias="externalObjectId", default=None,)
	externalObjectVersion: Optional[str] = Field(alias="externalObjectVersion", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)

from .planner_creation_source_kind import PlannerCreationSourceKind
from .planner_teams_publication_info import PlannerTeamsPublicationInfo
from .planner_external_task_source_display_type import PlannerExternalTaskSourceDisplayType

