from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFileThreatSubmissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecurityFileContentThreatSubmission, SecurityFileUrlThreatSubmission],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_file_content_threat_submission import SecurityFileContentThreatSubmission
from .security_file_url_threat_submission import SecurityFileUrlThreatSubmission

