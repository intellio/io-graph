from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcDisasterRecoveryAzureConnectionSetting(BaseModel):
	odata_type: Literal["#microsoft.graph.cloudPcDisasterRecoveryAzureConnectionSetting"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcDisasterRecoveryAzureConnectionSetting")
	onPremisesConnectionId: Optional[str] = Field(alias="onPremisesConnectionId", default=None,)

