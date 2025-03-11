from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCustodian(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	holdStatus: Optional[EdiscoveryDataSourceHoldStatus | str] = Field(alias="holdStatus",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	releasedDateTime: Optional[datetime] = Field(alias="releasedDateTime",default=None,)
	status: Optional[EdiscoveryDataSourceContainerStatus | str] = Field(alias="status",default=None,)
	lastIndexOperation: Optional[EdiscoveryCaseIndexOperation] = Field(alias="lastIndexOperation",default=None,)
	acknowledgedDateTime: Optional[datetime] = Field(alias="acknowledgedDateTime",default=None,)
	applyHoldToSources: Optional[bool] = Field(alias="applyHoldToSources",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	siteSources: Optional[list[EdiscoverySiteSource]] = Field(alias="siteSources",default=None,)
	unifiedGroupSources: Optional[list[EdiscoveryUnifiedGroupSource]] = Field(alias="unifiedGroupSources",default=None,)
	userSources: Optional[list[EdiscoveryUserSource]] = Field(alias="userSources",default=None,)

from .ediscovery_data_source_hold_status import EdiscoveryDataSourceHoldStatus
from .ediscovery_data_source_container_status import EdiscoveryDataSourceContainerStatus
from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
from .ediscovery_site_source import EdiscoverySiteSource
from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
from .ediscovery_user_source import EdiscoveryUserSource

