from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomAccessPackageWorkflowExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CustomAccessPackageWorkflowExtension]] = Field(alias="value", default=None,)

from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
