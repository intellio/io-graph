from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSite(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowRedirect: Optional[bool] = Field(alias="allowRedirect",default=None,)
	comment: Optional[str] = Field(alias="comment",default=None,)
	compatibilityMode: Optional[BrowserSiteCompatibilityMode | str] = Field(alias="compatibilityMode",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	history: Optional[list[BrowserSiteHistory]] = Field(alias="history",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	mergeType: Optional[BrowserSiteMergeType | str] = Field(alias="mergeType",default=None,)
	status: Optional[BrowserSiteStatus | str] = Field(alias="status",default=None,)
	targetEnvironment: Optional[BrowserSiteTargetEnvironment | str] = Field(alias="targetEnvironment",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)

from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
from .browser_site_history import BrowserSiteHistory
from .identity_set import IdentitySet
from .browser_site_merge_type import BrowserSiteMergeType
from .browser_site_status import BrowserSiteStatus
from .browser_site_target_environment import BrowserSiteTargetEnvironment

