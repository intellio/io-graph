from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryFile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	dateTime: Optional[datetime] = Field(alias="dateTime",default=None,)
	extension: Optional[str] = Field(alias="extension",default=None,)
	extractedTextContent: Optional[str] = Field(alias="extractedTextContent",default=None,)
	mediaType: Optional[str] = Field(alias="mediaType",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	otherProperties: Optional[SecurityStringValueDictionary] = Field(alias="otherProperties",default=None,)
	processingStatus: Optional[SecurityFileProcessingStatus | str] = Field(alias="processingStatus",default=None,)
	senderOrAuthors: Optional[list[str]] = Field(alias="senderOrAuthors",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	sourceType: Optional[SecuritySourceType | str] = Field(alias="sourceType",default=None,)
	subjectTitle: Optional[str] = Field(alias="subjectTitle",default=None,)
	custodian: Optional[SecurityEdiscoveryCustodian] = Field(alias="custodian",default=None,)
	tags: Optional[list[SecurityEdiscoveryReviewTag]] = Field(alias="tags",default=None,)

from .security_string_value_dictionary import SecurityStringValueDictionary
from .security_file_processing_status import SecurityFileProcessingStatus
from .security_source_type import SecuritySourceType
from .security_ediscovery_custodian import SecurityEdiscoveryCustodian
from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

