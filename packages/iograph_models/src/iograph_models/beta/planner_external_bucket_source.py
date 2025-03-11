from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerExternalBucketSource(BaseModel):
	creationSourceKind: Optional[PlannerCreationSourceKind | str] = Field(alias="creationSourceKind",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contextScenarioId: Optional[str] = Field(alias="contextScenarioId",default=None,)
	externalContextId: Optional[str] = Field(alias="externalContextId",default=None,)
	externalObjectId: Optional[str] = Field(alias="externalObjectId",default=None,)

from .planner_creation_source_kind import PlannerCreationSourceKind

