from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Agreement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.agreement"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isPerDeviceAcceptanceRequired: Optional[bool] = Field(alias="isPerDeviceAcceptanceRequired", default=None,)
	isViewingBeforeAcceptanceRequired: Optional[bool] = Field(alias="isViewingBeforeAcceptanceRequired", default=None,)
	termsExpiration: Optional[TermsExpiration] = Field(alias="termsExpiration", default=None,)
	userReacceptRequiredFrequency: Optional[str] = Field(alias="userReacceptRequiredFrequency", default=None,)
	acceptances: Optional[list[AgreementAcceptance]] = Field(alias="acceptances", default=None,)
	file: Optional[AgreementFile] = Field(alias="file", default=None,)
	files: Optional[list[AgreementFileLocalization]] = Field(alias="files", default=None,)

from .terms_expiration import TermsExpiration
from .agreement_acceptance import AgreementAcceptance
from .agreement_file import AgreementFile
from .agreement_file_localization import AgreementFileLocalization
