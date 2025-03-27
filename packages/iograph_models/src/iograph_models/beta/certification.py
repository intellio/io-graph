from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Certification(BaseModel):
	certificationDetailsUrl: Optional[str] = Field(alias="certificationDetailsUrl", default=None,)
	certificationExpirationDateTime: Optional[datetime] = Field(alias="certificationExpirationDateTime", default=None,)
	isCertifiedByMicrosoft: Optional[bool] = Field(alias="isCertifiedByMicrosoft", default=None,)
	isPublisherAttested: Optional[bool] = Field(alias="isPublisherAttested", default=None,)
	lastCertificationDateTime: Optional[datetime] = Field(alias="lastCertificationDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


