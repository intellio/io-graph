from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_planPostRequest(BaseModel):
	target: SerializeAsAny[Optional[BusinessScenarioTaskTargetBase]] = Field(alias="target",default=None,)

from .business_scenario_task_target_base import BusinessScenarioTaskTargetBase

