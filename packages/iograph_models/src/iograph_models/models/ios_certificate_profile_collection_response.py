from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosCertificateProfile] = Field(alias="value",)

from .ios_certificate_profile import IosCertificateProfile

