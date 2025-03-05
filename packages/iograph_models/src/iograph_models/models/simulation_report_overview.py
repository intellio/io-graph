from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationReportOverview(BaseModel):
	recommendedActions: Optional[list[RecommendedAction]] = Field(alias="recommendedActions",default=None,)
	resolvedTargetsCount: Optional[int] = Field(alias="resolvedTargetsCount",default=None,)
	simulationEventsContent: Optional[SimulationEventsContent] = Field(alias="simulationEventsContent",default=None,)
	trainingEventsContent: Optional[TrainingEventsContent] = Field(alias="trainingEventsContent",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .recommended_action import RecommendedAction
from .simulation_events_content import SimulationEventsContent
from .training_events_content import TrainingEventsContent

