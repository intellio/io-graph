from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ThreatAssessmentRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[EmailFileAssessmentRequest, FileAssessmentRequest, MailAssessmentRequest, UrlAssessmentRequest]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .email_file_assessment_request import EmailFileAssessmentRequest
from .file_assessment_request import FileAssessmentRequest
from .mail_assessment_request import MailAssessmentRequest
from .url_assessment_request import UrlAssessmentRequest

