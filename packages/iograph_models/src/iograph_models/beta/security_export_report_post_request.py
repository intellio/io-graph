from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_export_reportPostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	exportCriteria: Optional[SecurityExportCriteria | str] = Field(alias="exportCriteria", default=None,)
	exportLocation: Optional[SecurityExportLocation | str] = Field(alias="exportLocation", default=None,)
	additionalOptions: Optional[SecurityAdditionalOptions | str] = Field(alias="additionalOptions", default=None,)
	cloudAttachmentVersion: Optional[SecurityCloudAttachmentVersion | str] = Field(alias="cloudAttachmentVersion", default=None,)
	documentVersion: Optional[SecurityDocumentVersion | str] = Field(alias="documentVersion", default=None,)

from .security_export_criteria import SecurityExportCriteria
from .security_export_location import SecurityExportLocation
from .security_additional_options import SecurityAdditionalOptions
from .security_cloud_attachment_version import SecurityCloudAttachmentVersion
from .security_document_version import SecurityDocumentVersion
