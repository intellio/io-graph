from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerExternalPlanSource(BaseModel):
	creationSourceKind: Optional[PlannerCreationSourceKind | str] = Field(alias="creationSourceKind", default=None,)
	odata_type: Literal["#microsoft.graph.plannerExternalPlanSource"] = Field(alias="@odata.type", default="#microsoft.graph.plannerExternalPlanSource")
	contextScenarioId: Optional[str] = Field(alias="contextScenarioId", default=None,)
	externalContextId: Optional[str] = Field(alias="externalContextId", default=None,)
	externalObjectId: Optional[str] = Field(alias="externalObjectId", default=None,)

from .planner_creation_source_kind import PlannerCreationSourceKind

