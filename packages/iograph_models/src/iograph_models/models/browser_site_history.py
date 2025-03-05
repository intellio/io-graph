from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSiteHistory(BaseModel):
	allowRedirect: Optional[bool] = Field(alias="allowRedirect",default=None,)
	comment: Optional[str] = Field(alias="comment",default=None,)
	compatibilityMode: Optional[str | BrowserSiteCompatibilityMode] = Field(alias="compatibilityMode",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	mergeType: Optional[str | BrowserSiteMergeType] = Field(alias="mergeType",default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime",default=None,)
	targetEnvironment: Optional[str | BrowserSiteTargetEnvironment] = Field(alias="targetEnvironment",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
from .identity_set import IdentitySet
from .browser_site_merge_type import BrowserSiteMergeType
from .browser_site_target_environment import BrowserSiteTargetEnvironment

