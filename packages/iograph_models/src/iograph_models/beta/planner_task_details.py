from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class PlannerTaskDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerTaskDetails"] = Field(alias="@odata.type", default="#microsoft.graph.plannerTaskDetails")
	approvalAttachment: Optional[Union[PlannerBasicApprovalAttachment]] = Field(alias="approvalAttachment", default=None,discriminator="odata_type", )
	checklist: Optional[PlannerChecklistItems] = Field(alias="checklist", default=None,)
	completionRequirements: Optional[PlannerTaskCompletionRequirementDetails] = Field(alias="completionRequirements", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	forms: Optional[PlannerFormsDictionary] = Field(alias="forms", default=None,)
	notes: Optional[ItemBody] = Field(alias="notes", default=None,)
	previewType: Optional[PlannerPreviewType | str] = Field(alias="previewType", default=None,)
	references: Optional[PlannerExternalReferences] = Field(alias="references", default=None,)

from .planner_basic_approval_attachment import PlannerBasicApprovalAttachment
from .planner_checklist_items import PlannerChecklistItems
from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails
from .planner_forms_dictionary import PlannerFormsDictionary
from .item_body import ItemBody
from .planner_preview_type import PlannerPreviewType
from .planner_external_references import PlannerExternalReferences
