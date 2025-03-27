from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCustodian(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoveryCustodian"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoveryCustodian")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	holdStatus: Optional[SecurityDataSourceHoldStatus | str] = Field(alias="holdStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	releasedDateTime: Optional[datetime] = Field(alias="releasedDateTime", default=None,)
	status: Optional[SecurityDataSourceContainerStatus | str] = Field(alias="status", default=None,)
	acknowledgedDateTime: Optional[datetime] = Field(alias="acknowledgedDateTime", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	lastIndexOperation: Optional[SecurityEdiscoveryIndexOperation] = Field(alias="lastIndexOperation", default=None,)
	siteSources: Optional[list[SecuritySiteSource]] = Field(alias="siteSources", default=None,)
	unifiedGroupSources: Optional[list[SecurityUnifiedGroupSource]] = Field(alias="unifiedGroupSources", default=None,)
	userSources: Optional[list[SecurityUserSource]] = Field(alias="userSources", default=None,)

from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_data_source_container_status import SecurityDataSourceContainerStatus
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
from .security_site_source import SecuritySiteSource
from .security_unified_group_source import SecurityUnifiedGroupSource
from .security_user_source import SecurityUserSource

