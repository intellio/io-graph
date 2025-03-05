from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IntuneBrand(BaseModel):
	contactITEmailAddress: Optional[str] = Field(default=None,alias="contactITEmailAddress",)
	contactITName: Optional[str] = Field(default=None,alias="contactITName",)
	contactITNotes: Optional[str] = Field(default=None,alias="contactITNotes",)
	contactITPhoneNumber: Optional[str] = Field(default=None,alias="contactITPhoneNumber",)
	darkBackgroundLogo: Optional[MimeContent] = Field(default=None,alias="darkBackgroundLogo",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lightBackgroundLogo: Optional[MimeContent] = Field(default=None,alias="lightBackgroundLogo",)
	onlineSupportSiteName: Optional[str] = Field(default=None,alias="onlineSupportSiteName",)
	onlineSupportSiteUrl: Optional[str] = Field(default=None,alias="onlineSupportSiteUrl",)
	privacyUrl: Optional[str] = Field(default=None,alias="privacyUrl",)
	showDisplayNameNextToLogo: Optional[bool] = Field(default=None,alias="showDisplayNameNextToLogo",)
	showLogo: Optional[bool] = Field(default=None,alias="showLogo",)
	showNameNextToLogo: Optional[bool] = Field(default=None,alias="showNameNextToLogo",)
	themeColor: Optional[RgbColor] = Field(default=None,alias="themeColor",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .mime_content import MimeContent
from .mime_content import MimeContent
from .rgb_color import RgbColor

