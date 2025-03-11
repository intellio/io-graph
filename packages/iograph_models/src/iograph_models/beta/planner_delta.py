from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerDelta(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat":
				from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
				return PlannerAssignedToTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerBucket":
				from .planner_bucket import PlannerBucket
				return PlannerBucket.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerBucketTaskBoardTaskFormat":
				from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
				return PlannerBucketTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerPlan":
				from .planner_plan import PlannerPlan
				return PlannerPlan.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerPlanDetails":
				from .planner_plan_details import PlannerPlanDetails
				return PlannerPlanDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerProgressTaskBoardTaskFormat":
				from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
				return PlannerProgressTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerTask":
				from .planner_task import PlannerTask
				return PlannerTask.model_validate(data)
			if mapping_key == "#microsoft.graph.businessScenarioTask":
				from .business_scenario_task import BusinessScenarioTask
				return BusinessScenarioTask.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerTaskDetails":
				from .planner_task_details import PlannerTaskDetails
				return PlannerTaskDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerUser":
				from .planner_user import PlannerUser
				return PlannerUser.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


