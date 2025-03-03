from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSite(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowRedirect: Optional[bool] = Field(default=None,alias="allowRedirect",)
	comment: Optional[str] = Field(default=None,alias="comment",)
	compatibilityMode: Optional[BrowserSiteCompatibilityMode] = Field(default=None,alias="compatibilityMode",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	history: Optional[list[BrowserSiteHistory]] = Field(default=None,alias="history",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	mergeType: Optional[BrowserSiteMergeType] = Field(default=None,alias="mergeType",)
	status: Optional[BrowserSiteStatus] = Field(default=None,alias="status",)
	targetEnvironment: Optional[BrowserSiteTargetEnvironment] = Field(default=None,alias="targetEnvironment",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)

from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
from .browser_site_history import BrowserSiteHistory
from .identity_set import IdentitySet
from .browser_site_merge_type import BrowserSiteMergeType
from .browser_site_status import BrowserSiteStatus
from .browser_site_target_environment import BrowserSiteTargetEnvironment

