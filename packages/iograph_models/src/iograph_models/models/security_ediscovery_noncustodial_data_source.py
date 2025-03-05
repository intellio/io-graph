from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryNoncustodialDataSource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	holdStatus: Optional[SecurityDataSourceHoldStatus] = Field(default=None,alias="holdStatus",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	releasedDateTime: Optional[datetime] = Field(default=None,alias="releasedDateTime",)
	status: Optional[SecurityDataSourceContainerStatus] = Field(default=None,alias="status",)
	dataSource: Optional[SecurityDataSource] = Field(default=None,alias="dataSource",)
	lastIndexOperation: Optional[SecurityEdiscoveryIndexOperation] = Field(default=None,alias="lastIndexOperation",)

from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_data_source_container_status import SecurityDataSourceContainerStatus
from .security_data_source import SecurityDataSource
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation

