from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PublishedResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.publishedResource"] = Field(alias="@odata.type", default="#microsoft.graph.publishedResource")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	publishingType: Optional[OnPremisesPublishingType | str] = Field(alias="publishingType", default=None,)
	resourceName: Optional[str] = Field(alias="resourceName", default=None,)
	agentGroups: Optional[list[OnPremisesAgentGroup]] = Field(alias="agentGroups", default=None,)

from .on_premises_publishing_type import OnPremisesPublishingType
from .on_premises_agent_group import OnPremisesAgentGroup
