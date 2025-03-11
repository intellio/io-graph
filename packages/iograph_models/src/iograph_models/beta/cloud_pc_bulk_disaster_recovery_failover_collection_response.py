from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcBulkDisasterRecoveryFailoverCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CloudPcBulkDisasterRecoveryFailover]] = Field(alias="value",default=None,)

from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover

