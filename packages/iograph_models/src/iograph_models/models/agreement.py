from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Agreement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isPerDeviceAcceptanceRequired: Optional[bool] = Field(default=None,alias="isPerDeviceAcceptanceRequired",)
	isViewingBeforeAcceptanceRequired: Optional[bool] = Field(default=None,alias="isViewingBeforeAcceptanceRequired",)
	termsExpiration: Optional[TermsExpiration] = Field(default=None,alias="termsExpiration",)
	userReacceptRequiredFrequency: Optional[str] = Field(default=None,alias="userReacceptRequiredFrequency",)
	acceptances: list[AgreementAcceptance] = Field(alias="acceptances",)
	file: Optional[AgreementFile] = Field(default=None,alias="file",)
	files: list[AgreementFileLocalization] = Field(alias="files",)

from .terms_expiration import TermsExpiration
from .agreement_acceptance import AgreementAcceptance
from .agreement_file import AgreementFile
from .agreement_file_localization import AgreementFileLocalization

