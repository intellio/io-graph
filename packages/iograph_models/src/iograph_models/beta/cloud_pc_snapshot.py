from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcSnapshot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcSnapshot"] = Field(alias="@odata.type",)
	cloudPcId: Optional[str] = Field(alias="cloudPcId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastRestoredDateTime: Optional[datetime] = Field(alias="lastRestoredDateTime", default=None,)
	snapshotType: Optional[CloudPcSnapshotType | str] = Field(alias="snapshotType", default=None,)
	status: Optional[CloudPcSnapshotStatus | str] = Field(alias="status", default=None,)

from .cloud_pc_snapshot_type import CloudPcSnapshotType
from .cloud_pc_snapshot_status import CloudPcSnapshotStatus
