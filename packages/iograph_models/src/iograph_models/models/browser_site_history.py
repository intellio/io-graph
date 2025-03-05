from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSiteHistory(BaseModel):
	allowRedirect: Optional[bool] = Field(default=None,alias="allowRedirect",)
	comment: Optional[str] = Field(default=None,alias="comment",)
	compatibilityMode: Optional[BrowserSiteCompatibilityMode] = Field(default=None,alias="compatibilityMode",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	mergeType: Optional[BrowserSiteMergeType] = Field(default=None,alias="mergeType",)
	publishedDateTime: Optional[datetime] = Field(default=None,alias="publishedDateTime",)
	targetEnvironment: Optional[BrowserSiteTargetEnvironment] = Field(default=None,alias="targetEnvironment",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
from .identity_set import IdentitySet
from .browser_site_merge_type import BrowserSiteMergeType
from .browser_site_target_environment import BrowserSiteTargetEnvironment

