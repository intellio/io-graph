from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LogicAppTriggerEndpointConfiguration(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	logicAppWorkflowName: Optional[str] = Field(alias="logicAppWorkflowName",default=None,)
	resourceGroupName: Optional[str] = Field(alias="resourceGroupName",default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)


