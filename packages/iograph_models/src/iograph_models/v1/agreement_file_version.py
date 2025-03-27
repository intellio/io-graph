from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AgreementFileVersion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fileData: Optional[AgreementFileData] = Field(alias="fileData", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isMajorVersion: Optional[bool] = Field(alias="isMajorVersion", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)

from .agreement_file_data import AgreementFileData

