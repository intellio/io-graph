from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IntuneBrand(BaseModel):
	contactITEmailAddress: Optional[str] = Field(alias="contactITEmailAddress",default=None,)
	contactITName: Optional[str] = Field(alias="contactITName",default=None,)
	contactITNotes: Optional[str] = Field(alias="contactITNotes",default=None,)
	contactITPhoneNumber: Optional[str] = Field(alias="contactITPhoneNumber",default=None,)
	darkBackgroundLogo: Optional[MimeContent] = Field(alias="darkBackgroundLogo",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lightBackgroundLogo: Optional[MimeContent] = Field(alias="lightBackgroundLogo",default=None,)
	onlineSupportSiteName: Optional[str] = Field(alias="onlineSupportSiteName",default=None,)
	onlineSupportSiteUrl: Optional[str] = Field(alias="onlineSupportSiteUrl",default=None,)
	privacyUrl: Optional[str] = Field(alias="privacyUrl",default=None,)
	showDisplayNameNextToLogo: Optional[bool] = Field(alias="showDisplayNameNextToLogo",default=None,)
	showLogo: Optional[bool] = Field(alias="showLogo",default=None,)
	showNameNextToLogo: Optional[bool] = Field(alias="showNameNextToLogo",default=None,)
	themeColor: Optional[RgbColor] = Field(alias="themeColor",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .mime_content import MimeContent
from .mime_content import MimeContent
from .rgb_color import RgbColor

