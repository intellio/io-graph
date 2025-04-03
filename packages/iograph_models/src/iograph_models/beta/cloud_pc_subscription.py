from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcSubscription(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcSubscription"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcSubscription")
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)
	subscriptionName: Optional[str] = Field(alias="subscriptionName", default=None,)

