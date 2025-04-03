from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnPremisesAgent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onPremisesAgent"] = Field(alias="@odata.type", default="#microsoft.graph.onPremisesAgent")
	externalIp: Optional[str] = Field(alias="externalIp", default=None,)
	machineName: Optional[str] = Field(alias="machineName", default=None,)
	status: Optional[AgentStatus | str] = Field(alias="status", default=None,)
	supportedPublishingTypes: Optional[list[OnPremisesPublishingType | str]] = Field(alias="supportedPublishingTypes", default=None,)
	agentGroups: Optional[list[OnPremisesAgentGroup]] = Field(alias="agentGroups", default=None,)

from .agent_status import AgentStatus
from .on_premises_publishing_type import OnPremisesPublishingType
from .on_premises_agent_group import OnPremisesAgentGroup
