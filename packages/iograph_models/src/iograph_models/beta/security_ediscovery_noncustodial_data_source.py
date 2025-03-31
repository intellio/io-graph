from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoveryNoncustodialDataSource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoveryNoncustodialDataSource"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoveryNoncustodialDataSource")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	holdStatus: Optional[SecurityDataSourceHoldStatus | str] = Field(alias="holdStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	releasedDateTime: Optional[datetime] = Field(alias="releasedDateTime", default=None,)
	status: Optional[SecurityDataSourceContainerStatus | str] = Field(alias="status", default=None,)
	dataSource: Optional[Union[SecuritySiteSource, SecurityUnifiedGroupSource, SecurityUserSource]] = Field(alias="dataSource", default=None,discriminator="odata_type", )
	lastIndexOperation: Optional[SecurityEdiscoveryIndexOperation] = Field(alias="lastIndexOperation", default=None,)

from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_data_source_container_status import SecurityDataSourceContainerStatus
from .security_site_source import SecuritySiteSource
from .security_unified_group_source import SecurityUnifiedGroupSource
from .security_user_source import SecurityUserSource
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
