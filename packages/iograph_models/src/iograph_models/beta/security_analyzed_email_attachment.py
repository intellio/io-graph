from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAnalyzedEmailAttachment(BaseModel):
	detonationDetails: Optional[SecurityDetonationDetails] = Field(alias="detonationDetails", default=None,)
	fileExtension: Optional[str] = Field(alias="fileExtension", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	fileSize: Optional[int] = Field(alias="fileSize", default=None,)
	fileType: Optional[str] = Field(alias="fileType", default=None,)
	malwareFamily: Optional[str] = Field(alias="malwareFamily", default=None,)
	sha256: Optional[str] = Field(alias="sha256", default=None,)
	tenantAllowBlockListDetailInfo: Optional[str] = Field(alias="tenantAllowBlockListDetailInfo", default=None,)
	threatType: Optional[SecurityThreatType | str] = Field(alias="threatType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_detonation_details import SecurityDetonationDetails
from .security_threat_type import SecurityThreatType
