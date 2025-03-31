from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnPremisesAgentGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onPremisesAgentGroup"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	publishingType: Optional[OnPremisesPublishingType | str] = Field(alias="publishingType", default=None,)
	agents: Optional[list[OnPremisesAgent]] = Field(alias="agents", default=None,)
	publishedResources: Optional[list[PublishedResource]] = Field(alias="publishedResources", default=None,)

from .on_premises_publishing_type import OnPremisesPublishingType
from .on_premises_agent import OnPremisesAgent
from .published_resource import PublishedResource
