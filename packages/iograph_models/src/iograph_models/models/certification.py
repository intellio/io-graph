from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Certification(BaseModel):
	certificationDetailsUrl: Optional[str] = Field(default=None,alias="certificationDetailsUrl",)
	certificationExpirationDateTime: Optional[datetime] = Field(default=None,alias="certificationExpirationDateTime",)
	isCertifiedByMicrosoft: Optional[bool] = Field(default=None,alias="isCertifiedByMicrosoft",)
	isPublisherAttested: Optional[bool] = Field(default=None,alias="isPublisherAttested",)
	lastCertificationDateTime: Optional[datetime] = Field(default=None,alias="lastCertificationDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


