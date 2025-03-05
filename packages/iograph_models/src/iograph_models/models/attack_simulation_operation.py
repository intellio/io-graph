from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AttackSimulationOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	resourceLocation: Optional[str] = Field(default=None,alias="resourceLocation",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)
	statusDetail: Optional[str] = Field(default=None,alias="statusDetail",)
	percentageCompleted: Optional[int] = Field(default=None,alias="percentageCompleted",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	type: Optional[AttackSimulationOperationType] = Field(default=None,alias="type",)

from .long_running_operation_status import LongRunningOperationStatus
from .attack_simulation_operation_type import AttackSimulationOperationType

