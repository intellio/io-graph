from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CustomExtensionHandler(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.customExtensionHandler"] = Field(alias="@odata.type",)
	stage: Optional[AccessPackageCustomExtensionStage | str] = Field(alias="stage", default=None,)
	customExtension: Optional[CustomAccessPackageWorkflowExtension] = Field(alias="customExtension", default=None,)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
