from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequestCallbackData(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	customExtensionStageInstanceDetail: Optional[str] = Field(default=None,alias="customExtensionStageInstanceDetail",)
	customExtensionStageInstanceId: Optional[str] = Field(default=None,alias="customExtensionStageInstanceId",)
	stage: Optional[AccessPackageCustomExtensionStage] = Field(default=None,alias="stage",)
	state: Optional[str] = Field(default=None,alias="state",)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage

