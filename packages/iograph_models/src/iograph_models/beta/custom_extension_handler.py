from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionHandler(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	stage: Optional[AccessPackageCustomExtensionStage | str] = Field(alias="stage", default=None,)
	customExtension: Optional[CustomAccessPackageWorkflowExtension] = Field(alias="customExtension", default=None,)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension

