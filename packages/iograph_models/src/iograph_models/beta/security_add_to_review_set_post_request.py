from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_add_to_review_setPostRequest(BaseModel):
	search: Optional[SecurityEdiscoverySearch] = Field(alias="search", default=None,)
	additionalDataOptions: Optional[SecurityAdditionalDataOptions | str] = Field(alias="additionalDataOptions", default=None,)
	itemsToInclude: Optional[SecurityItemsToInclude | str] = Field(alias="itemsToInclude", default=None,)
	cloudAttachmentVersion: Optional[SecurityCloudAttachmentVersion | str] = Field(alias="cloudAttachmentVersion", default=None,)
	documentVersion: Optional[SecurityDocumentVersion | str] = Field(alias="documentVersion", default=None,)

from .security_ediscovery_search import SecurityEdiscoverySearch
from .security_additional_data_options import SecurityAdditionalDataOptions
from .security_items_to_include import SecurityItemsToInclude
from .security_cloud_attachment_version import SecurityCloudAttachmentVersion
from .security_document_version import SecurityDocumentVersion

