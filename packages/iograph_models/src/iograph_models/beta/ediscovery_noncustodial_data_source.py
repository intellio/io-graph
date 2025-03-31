from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EdiscoveryNoncustodialDataSource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ediscovery.noncustodialDataSource"] = Field(alias="@odata.type", default="#microsoft.graph.ediscovery.noncustodialDataSource")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	holdStatus: Optional[EdiscoveryDataSourceHoldStatus | str] = Field(alias="holdStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	releasedDateTime: Optional[datetime] = Field(alias="releasedDateTime", default=None,)
	status: Optional[EdiscoveryDataSourceContainerStatus | str] = Field(alias="status", default=None,)
	lastIndexOperation: Optional[EdiscoveryCaseIndexOperation] = Field(alias="lastIndexOperation", default=None,)
	applyHoldToSource: Optional[bool] = Field(alias="applyHoldToSource", default=None,)
	dataSource: Optional[Union[EdiscoverySiteSource, EdiscoveryUnifiedGroupSource, EdiscoveryUserSource]] = Field(alias="dataSource", default=None,discriminator="odata_type", )

from .ediscovery_data_source_hold_status import EdiscoveryDataSourceHoldStatus
from .ediscovery_data_source_container_status import EdiscoveryDataSourceContainerStatus
from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
from .ediscovery_site_source import EdiscoverySiteSource
from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
from .ediscovery_user_source import EdiscoveryUserSource
