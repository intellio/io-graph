from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtection(BaseModel):
	bitlocker: Optional[Bitlocker] = Field(alias="bitlocker", default=None,)
	threatAssessmentRequests: Optional[list[Annotated[Union[EmailFileAssessmentRequest, FileAssessmentRequest, MailAssessmentRequest, UrlAssessmentRequest]],Field(discriminator="odata_type")]]] = Field(alias="threatAssessmentRequests", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .bitlocker import Bitlocker
from .email_file_assessment_request import EmailFileAssessmentRequest
from .file_assessment_request import FileAssessmentRequest
from .mail_assessment_request import MailAssessmentRequest
from .url_assessment_request import UrlAssessmentRequest

