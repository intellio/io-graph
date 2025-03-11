from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcSnapshot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudPcId: Optional[str] = Field(alias="cloudPcId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	lastRestoredDateTime: Optional[datetime] = Field(alias="lastRestoredDateTime",default=None,)
	snapshotType: Optional[CloudPcSnapshotType | str] = Field(alias="snapshotType",default=None,)
	status: Optional[CloudPcSnapshotStatus | str] = Field(alias="status",default=None,)

from .cloud_pc_snapshot_type import CloudPcSnapshotType
from .cloud_pc_snapshot_status import CloudPcSnapshotStatus

