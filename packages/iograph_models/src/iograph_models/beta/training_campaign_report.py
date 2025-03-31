from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrainingCampaignReport(BaseModel):
	campaignUsers: Optional[list[UserSimulationDetails]] = Field(alias="campaignUsers", default=None,)
	overview: Optional[TrainingCampaignReportOverview] = Field(alias="overview", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_simulation_details import UserSimulationDetails
from .training_campaign_report_overview import TrainingCampaignReportOverview
