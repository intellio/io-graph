from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequestCallbackData(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	customExtensionStageInstanceDetail: Optional[str] = Field(alias="customExtensionStageInstanceDetail",default=None,)
	customExtensionStageInstanceId: Optional[str] = Field(alias="customExtensionStageInstanceId",default=None,)
	stage: Optional[str | AccessPackageCustomExtensionStage] = Field(alias="stage",default=None,)
	state: Optional[str] = Field(alias="state",default=None,)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage

