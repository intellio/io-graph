from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidEnrollmentCompanyCode(BaseModel):
	enrollmentToken: Optional[str] = Field(alias="enrollmentToken", default=None,)
	qrCodeContent: Optional[str] = Field(alias="qrCodeContent", default=None,)
	qrCodeImage: Optional[MimeContent] = Field(alias="qrCodeImage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .mime_content import MimeContent

