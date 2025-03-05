from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AgreementFile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	fileData: Optional[AgreementFileData] = Field(default=None,alias="fileData",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	isMajorVersion: Optional[bool] = Field(default=None,alias="isMajorVersion",)
	language: Optional[str] = Field(default=None,alias="language",)
	localizations: Optional[list[AgreementFileLocalization]] = Field(default=None,alias="localizations",)

from .agreement_file_data import AgreementFileData
from .agreement_file_localization import AgreementFileLocalization

