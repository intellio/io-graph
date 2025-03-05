from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationReportOverview(BaseModel):
	recommendedActions: Optional[list[RecommendedAction]] = Field(default=None,alias="recommendedActions",)
	resolvedTargetsCount: Optional[int] = Field(default=None,alias="resolvedTargetsCount",)
	simulationEventsContent: Optional[SimulationEventsContent] = Field(default=None,alias="simulationEventsContent",)
	trainingEventsContent: Optional[TrainingEventsContent] = Field(default=None,alias="trainingEventsContent",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recommended_action import RecommendedAction
from .simulation_events_content import SimulationEventsContent
from .training_events_content import TrainingEventsContent

