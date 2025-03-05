from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryNoncustodialDataSource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	holdStatus: Optional[str | SecurityDataSourceHoldStatus] = Field(alias="holdStatus",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	releasedDateTime: Optional[datetime] = Field(alias="releasedDateTime",default=None,)
	status: Optional[str | SecurityDataSourceContainerStatus] = Field(alias="status",default=None,)
	dataSource: SerializeAsAny[Optional[SecurityDataSource]] = Field(alias="dataSource",default=None,)
	lastIndexOperation: Optional[SecurityEdiscoveryIndexOperation] = Field(alias="lastIndexOperation",default=None,)

from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_data_source_container_status import SecurityDataSourceContainerStatus
from .security_data_source import SecurityDataSource
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation

