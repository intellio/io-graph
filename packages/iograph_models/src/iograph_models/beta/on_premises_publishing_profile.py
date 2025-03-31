from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnPremisesPublishingProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onPremisesPublishingProfile"] = Field(alias="@odata.type",)
	hybridAgentUpdaterConfiguration: Optional[HybridAgentUpdaterConfiguration] = Field(alias="hybridAgentUpdaterConfiguration", default=None,)
	isDefaultAccessEnabled: Optional[bool] = Field(alias="isDefaultAccessEnabled", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	agentGroups: Optional[list[OnPremisesAgentGroup]] = Field(alias="agentGroups", default=None,)
	agents: Optional[list[OnPremisesAgent]] = Field(alias="agents", default=None,)
	applicationSegments: Optional[list[IpApplicationSegment]] = Field(alias="applicationSegments", default=None,)
	connectorGroups: Optional[list[ConnectorGroup]] = Field(alias="connectorGroups", default=None,)
	connectors: Optional[list[Connector]] = Field(alias="connectors", default=None,)
	publishedResources: Optional[list[PublishedResource]] = Field(alias="publishedResources", default=None,)

from .hybrid_agent_updater_configuration import HybridAgentUpdaterConfiguration
from .on_premises_agent_group import OnPremisesAgentGroup
from .on_premises_agent import OnPremisesAgent
from .ip_application_segment import IpApplicationSegment
from .connector_group import ConnectorGroup
from .connector import Connector
from .published_resource import PublishedResource
