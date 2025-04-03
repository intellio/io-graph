from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AttackSimulationOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.attackSimulationOperation"] = Field(alias="@odata.type", default="#microsoft.graph.attackSimulationOperation")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status", default=None,)
	statusDetail: Optional[str] = Field(alias="statusDetail", default=None,)
	percentageCompleted: Optional[int] = Field(alias="percentageCompleted", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	type: Optional[AttackSimulationOperationType | str] = Field(alias="type", default=None,)

from .long_running_operation_status import LongRunningOperationStatus
from .attack_simulation_operation_type import AttackSimulationOperationType
