from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoveryCustodian(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	holdStatus: Optional[SecurityDataSourceHoldStatus] = Field(default=None,alias="holdStatus",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	releasedDateTime: Optional[datetime] = Field(default=None,alias="releasedDateTime",)
	status: Optional[SecurityDataSourceContainerStatus] = Field(default=None,alias="status",)
	acknowledgedDateTime: Optional[datetime] = Field(default=None,alias="acknowledgedDateTime",)
	email: Optional[str] = Field(default=None,alias="email",)
	lastIndexOperation: Optional[SecurityEdiscoveryIndexOperation] = Field(default=None,alias="lastIndexOperation",)
	siteSources: Optional[list[SecuritySiteSource]] = Field(default=None,alias="siteSources",)
	unifiedGroupSources: Optional[list[SecurityUnifiedGroupSource]] = Field(default=None,alias="unifiedGroupSources",)
	userSources: Optional[list[SecurityUserSource]] = Field(default=None,alias="userSources",)

from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .security_data_source_container_status import SecurityDataSourceContainerStatus
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
from .security_site_source import SecuritySiteSource
from .security_unified_group_source import SecurityUnifiedGroupSource
from .security_user_source import SecurityUserSource

