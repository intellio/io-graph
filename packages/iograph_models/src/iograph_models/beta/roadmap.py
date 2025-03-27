from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Roadmap(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.roadmap"] = Field(alias="@odata.type", default="#microsoft.graph.roadmap")
	changeItemService: Optional[str] = Field(alias="changeItemService", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	documentationUrls: Optional[list[str]] = Field(alias="documentationUrls", default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription", default=None,)
	systemTags: Optional[list[str]] = Field(alias="systemTags", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	category: Optional[str] = Field(alias="category", default=None,)
	changeItemState: Optional[ChangeItemState | str] = Field(alias="changeItemState", default=None,)
	deliveryStage: Optional[RoadmapItemDeliveryStage | str] = Field(alias="deliveryStage", default=None,)
	gotoLink: Optional[str] = Field(alias="gotoLink", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)

from .change_item_state import ChangeItemState
from .roadmap_item_delivery_stage import RoadmapItemDeliveryStage

