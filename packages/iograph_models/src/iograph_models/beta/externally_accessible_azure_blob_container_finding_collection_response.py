from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternallyAccessibleAzureBlobContainerFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ExternallyAccessibleAzureBlobContainerFinding]] = Field(alias="value",default=None,)

from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding

