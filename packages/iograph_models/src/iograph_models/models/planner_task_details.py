from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskDetails(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	checklist: Optional[PlannerChecklistItems] = Field(default=None,alias="checklist",)
	description: Optional[str] = Field(default=None,alias="description",)
	previewType: Optional[PlannerPreviewType] = Field(default=None,alias="previewType",)
	references: Optional[PlannerExternalReferences] = Field(default=None,alias="references",)

from .planner_checklist_items import PlannerChecklistItems
from .planner_preview_type import PlannerPreviewType
from .planner_external_references import PlannerExternalReferences

