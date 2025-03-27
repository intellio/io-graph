from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	checklist: Optional[PlannerChecklistItems] = Field(alias="checklist", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	previewType: Optional[PlannerPreviewType | str] = Field(alias="previewType", default=None,)
	references: Optional[PlannerExternalReferences] = Field(alias="references", default=None,)

from .planner_checklist_items import PlannerChecklistItems
from .planner_preview_type import PlannerPreviewType
from .planner_external_references import PlannerExternalReferences

