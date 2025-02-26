from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LogicAppTriggerEndpointConfiguration(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	logicAppWorkflowName: Optional[str] = Field(default=None,alias="logicAppWorkflowName",)
	resourceGroupName: Optional[str] = Field(default=None,alias="resourceGroupName",)
	subscriptionId: Optional[str] = Field(default=None,alias="subscriptionId",)
	url: Optional[str] = Field(default=None,alias="url",)


