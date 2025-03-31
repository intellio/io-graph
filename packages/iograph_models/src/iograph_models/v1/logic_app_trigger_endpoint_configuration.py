from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class LogicAppTriggerEndpointConfiguration(BaseModel):
	odata_type: Literal["#microsoft.graph.logicAppTriggerEndpointConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.logicAppTriggerEndpointConfiguration")
	logicAppWorkflowName: Optional[str] = Field(alias="logicAppWorkflowName", default=None,)
	resourceGroupName: Optional[str] = Field(alias="resourceGroupName", default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)

